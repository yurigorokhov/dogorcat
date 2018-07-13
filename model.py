from keras.layers import Dropout, Flatten, Dense, BatchNormalization, Activation
from keras.models import Model
from keras import optimizers
from keras.applications import inception_v3

import tensorflow as tf

checkpoint_filename = 'checkpoints/checkpoint.h5'
classes = ['cats', 'dogs']
out = './out'


def sigmoid_crossentropy(output, target):
    return tf.nn.sigmoid_cross_entropy_with_logits(
        labels=target,
        logits=output
    )

def get_model():

    # Initialize inception model
    inception = inception_v3.InceptionV3(
        weights='imagenet',
        include_top=False,
        input_shape=(150, 150, 3)
    )

    # freeze all layers InceptionV3
    for layer in inception.layers:
        layer.trainable = False

    # add dense layers
    x = inception.output
    x = Flatten()(x)
    x = Dense(1024)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(512)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dense(128)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    predictions = Dense(len(classes), activation='sigmoid')(x)

    # create model
    model = Model(input=inception.input, output=predictions)
    model.compile(
        loss=sigmoid_crossentropy,
        optimizer=optimizers.Adam(lr=0.001),
        metrics=['accuracy']
    )
    return model


def get_rotation_model():

    # Initialize inception model
    inception = inception_v3.InceptionV3(
        weights='imagenet',
        include_top=False,
        input_shape=(150, 150, 3)
    )

    # freeze all layers InceptionV3
    for layer in inception.layers:
        layer.trainable = False

    # add dense layers
    x = inception.output
    x = Flatten()(x)
    x = Dense(1024)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(512)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = Dense(128)(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    predictions = Dense(len(rotation_classes), activation='sigmoid')(x)

    # create model
    model = Model(input=inception.input, output=predictions)
    model.compile(
        loss=sigmoid_crossentropy,
        optimizer=optimizers.Adam(lr=0.001),
        metrics=['accuracy']
    )
    return model