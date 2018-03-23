import argparse
import cv2
import numpy as np
import os.path

from model import get_model, checkpoint_filename, classes


def main():
    parser = argparse.ArgumentParser(description='Classify images')
    parser.add_argument('images', metavar='IMAGE', type=str, nargs='+',
                        help='image paths')
    args = parser.parse_args()
    image_paths = [os.path.abspath(img) for img in args.images]

    # load model weights
    if not os.path.isfile(checkpoint_filename):
        print('ERROR: model checkpoint does not exist, please run training first: python train.py')
        exit()
    print('INFO: loading model and weights')
    model = get_model()
    model.load_weights(checkpoint_filename)

    # predict
    for img_path in image_paths:

        # load and resize image
        img = cv2.imread(img_path)
        if img.shape[0] < 150 or img.shape[1] < 150:
            print('WARN: skipping image {} because it is smaller than 150px by 150px'.format(img_path))
            continue

        # resize image
        resized_image = cv2.resize(img, (150, 150))
        tensor = resized_image[None, :, :, :]

        # normalize pixel values
        tensor = np.divide(tensor, 255.0)

        # predict
        prediction = model.predict(tensor)
        print('Prediction for {}:'.format(img_path))
        for i, c in enumerate(classes):
            print('Class {}: {}%'.format(c, round(prediction[0][i]*100, 1)))


if __name__ == "__main__":
    main()
