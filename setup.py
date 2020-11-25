import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="InsightFace",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = {'InsightFace', 'InsightFace.retinaface', 'InsightFace.retinaface.data', 'InsightFace.retinaface.layers', 'InsightFace.retinaface.layers.functions', 'InsightFace.retinaface.layers.modules', 'InsightFace.retinaface.models', 'InsightFace.retinaface.utils', 'InsightFace.retinaface.utils.nms'},
    package_dir = {'InsightFace': '.', 'InsightFace.retinaface': 'retinaface', 'InsightFace.retinaface.data': 'retinaface/data', 'InsightFace.retinaface.layers': 'retinaface/layers', 'InsightFace.retinaface.layers.functions': 'retinaface/layers/functions', 'InsightFace.retinaface.layers.modules': 'retinaface/layers/modules', 'InsightFace.retinaface.models': 'retinaface/models', 'InsightFace.retinaface.utils': 'retinaface/utils', 'InsightFace.retinaface.utils.nms': 'retinaface/utils/nms'},
    python_requires='>=3.6',
    data_files = [('InsightFace/weights',
                    ['weights/w18.tar',
                     'weights/w50.tar',
                     'weights/w101.tar']),
                  ('InsightFace/retinaface/weights',
                    ['retinaface/weights/mobilenet0.25_Final.pth'])
                 ]
)