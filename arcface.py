import sys
import os
#sys.path.append(os.pardir)
from PIL import Image
import torch
from . import config
from tqdm import tqdm
import numpy as np
from .utils import align_face
from torchvision import transforms

def _no_grad(func):
    def wrapper(*args, **kwargs):
        with torch.no_grad():
            return func(*args, **kwargs)
        
    return wrapper

class ArcFace():
    def __init__(self, layers=50, batch_size=4):
        self.device = config.device
        self.layers = layers
        self.batch_size = batch_size

        d = os.path.dirname(__file__)
        
        if layers in (18, 50, 101):
            checkpoint_path = os.path.join(d, 'weights', 'w{}.tar'.format(layers))
        else:
            raise ValueError("Invalid number of layers: {}. Must be one of: 18, 50, 101."-format(layers))
        checkpoint = torch.load(checkpoint_path)
        self.model = checkpoint['model'].module.eval().to(self.device)

    def _preprocess(self, img, landmarks):
        if img.mode != "RGB":
            img = img.convert("RGB")
        img = align_face(img, landmarks)
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        img = transform(img)
        return img

    @_no_grad
    def extract(self, images, landmarks):
        if len(images) == 0:
            return np.array([])
        all_features = []
        for start_idx in tqdm(range(0, len(images), self.batch_size)):
            end_idx = min(len(images), start_idx + self.batch_size)
            length = end_idx - start_idx

            imgs = torch.zeros([length, 3, 112, 112], dtype=torch.float)
            for idx in range(0, length):
                i = start_idx + idx
                img = images[i]
                imgs[idx] = self._preprocess(img, landmarks[i])

            all_features.append(self.model(imgs.to(self.device)).cpu().numpy())
        return np.concatenate(all_features)
            
