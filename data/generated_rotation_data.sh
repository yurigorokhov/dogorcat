#!/usr/bin/env bash

if [ ! -d "./train" ]; then
    echo './train does not exist; please run ./download.sh first'
    exit 1
fi

if [ ! -d "./validation" ]; then
    echo './validation does not exist; please run ./download.sh first'
    exit 1
fi

if [ -d "./rotated_train" ]; then
    echo './rotated_train already exists, nothing to do'
else
    echo 'Generating ./rotated_train'

    # create directories
    mkdir -p ./rotated_train/deg_0
    mkdir -p ./rotated_train/deg_90
    mkdir -p ./rotated_train/deg_180
    mkdir -p ./rotated_train/deg_270

    # copy over files
    echo 'Copying and rotating files'
    rsync -av ./train/dogs/ ./rotated_train/deg_0/ >> /dev/null
    rsync -av ./train/cats/ ./rotated_train/deg_0/ >> /dev/null

    find ./train -iname "*.jpg" -exec sh -c 'convert -rotate "90" "{}" ./rotated_train/deg_90/`basename "{}"` ' \;
    find ./train -iname "*.jpg" -exec sh -c 'convert -rotate "180" "{}" ./rotated_train/deg_180/`basename "{}"` ' \;
    find ./train -iname "*.jpg" -exec sh -c 'convert -rotate "270" "{}" ./rotated_train/deg_270/`basename "{}"` ' \;   
fi

if [ -d "./rotated_validation" ]; then
    echo './rotated_validation already exists, nothing to do'
else
    echo 'Generating ./rotated_validation'
    exit 0
    # create directories
    mkdir -p ./rotated_validation/deg_0
    mkdir -p ./rotated_validation/deg_90
    mkdir -p ./rotated_validation/deg_180
    mkdir -p ./rotated_validation/deg_270

    # copy over files
    echo 'Copying files'
    rsync -av ./validation/dogs/ ./rotated_validation/deg_0/ >> /dev/null
    rsync -av ./validation/cats/ ./rotated_validation/deg_0/ >> /dev/null
    rsync -av ./validation/dogs/ ./rotated_validation/deg_90/ >> /dev/null
    rsync -av ./validation/cats/ ./rotated_validation/deg_90/ >> /dev/null
    rsync -av ./validation/dogs/ ./rotated_validation/deg_180/ >> /dev/null
    rsync -av ./validation/cats/ ./rotated_validation/deg_180/ >> /dev/null
    rsync -av ./validation/dogs/ ./rotated_validation/deg_270/ >> /dev/null
    rsync -av ./validation/cats/ ./rotated_validation/deg_270/ >> /dev/null

    # perform rotations
    echo 'Rotating images'
    find ./rotated_validation/deg_90/ -iname '*.jpg' -exec sh -c 'mogrify -rotate "90" "{}"' \;
    find ./rotated_validation/deg_180/ -iname '*.jpg' -exec sh -c 'mogrify -rotate "180" "{}"' \;
    find ./rotated_validation/deg_270/ -iname '*.jpg' -exec sh -c 'mogrify -rotate "270" "{}"' \;
fi