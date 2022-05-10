import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()

import time, os, io
import argparse, socket

import cv2
from PIL import Image

import keras
from keras.models import Sequential, Model, load_model
from keras.utils import np_utils
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.layers import Input, Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense, Lambda, concatenate
from keras.optimizers import Adam
from keras import backend as K

import tensorflow as tf
import numpy as np

from agent import Agent, random_agent

import collections

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

parser = argparse.ArgumentParser(description='Remote Driving')
parser.add_argument('--host', type=str, default='192.168.0.199', help='IP of host')
parser.add_argument('--port', type=int,
