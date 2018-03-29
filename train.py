from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping

from model import get_model, checkpoint_filename, classes
from util import plot_history


def main():
    batch_size = 16

    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
        'data/train',
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode='categorical',
        classes=classes
    )

    validation_generator = test_datagen.flow_from_directory(
        'data/validation',
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode='categorical',
        classes=classes
    )

    # check point the model
    checkpoint_callback = ModelCheckpoint(
        checkpoint_filename,
        monitor='val_loss',
        verbose=0,
        save_best_only=True,
        save_weights_only=False,
        mode='auto',
        period=1
    )

    # train the model
    model = get_model()
    print('Training...')
    history = model.fit_generator(
        train_generator,
        steps_per_epoch=50,
        epochs=20,
        validation_data=validation_generator,
        validation_steps=200,
        use_multiprocessing=True,
        shuffle=True,
        callbacks=[checkpoint_callback]
    )
    plot_history(history, out_dir='./out')


if __name__ == "__main__":
    main()
