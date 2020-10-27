import sys, os
sys.path.append(os.path.dirname(__file__)) # necessary to load the pickled model weights, since they were created without a package structure
from .arcface import ArcFace
