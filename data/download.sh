#!/usr/bin/env bash

# download
wget https://s3.amazonaws.com/yurig-public/train.tar.gz
wget https://s3.amazonaws.com/yurig-public/validation.tar.gz

# extract
tar zxvf train.tar.gz
tar zxvf validation.tar.gz