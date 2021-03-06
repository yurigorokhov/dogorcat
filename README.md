Cat or Dog
==========

Model based on InceptionV3 pre-trained on ImageNet, with last few layers refined on cat/dog images.

Installation
============
```bash
pip install -r requirements.txt
```

Data
====
```bash
cd data
./download.sh
```

Train
=====
```bash
python train.py
```

Accuracy/Loss
=============

These images will be saved in `./out/`

![alt text](./accuracy.png "Accuracy")
![alt text](./loss.png "Loss")


Classify some images
====================

```bash
python classify_images.py data/test_images/*
```

![alt text](./data/test_images/catordog.jpg "Image 1")

```
Prediction for data/test_images/catordog.jpg:
Class cats: 99.6%
Class dogs: 0.4%
```

![alt text](./data/test_images/catordog2.jpg "Image 2")

```
Prediction for data/test_images/catordog2.jpg:
Class cats: 0.4%
Class dogs: 99.6%
```

![alt text](./data/test_images/eski.jpg "Eski!")

```
Prediction for data/test_images/eski.jpg:
Class cats: 0.0%
Class dogs: 100.0%
```
