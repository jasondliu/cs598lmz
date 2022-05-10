import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os
import sys
import time
import argparse
import subprocess
import shutil
import math
import re

from PIL import Image, ImageDraw, ImageFont

import numpy as np
import cv2

from matplotlib import pyplot as plt

import json
import pickle

import util

from util import *

import tensorflow as tf

from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Input, Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization, Activation, Reshape, Conv2DTranspose, UpSampling2D
from tensorflow.keras.utils import plot_model

from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

from tensorflow.keras.optimizers import Adam

from tensorflow.keras.
