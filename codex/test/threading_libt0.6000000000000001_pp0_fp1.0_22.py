import threading
threading.stack_size(2**27)
import sys
import pygame
import time
from pygame.locals import *
from PIL import Image, ImageDraw, ImageFont
import os
import math
import traceback
import random
import string
import numpy as np
import tensorflow as tf
import cv2
import pyscreenshot as ImageGrab

from model import Model
from utils import *

def predict():
    # model = tf.keras.models.load_model('model_weights/model.h5')
    print("start predict")
    model = Model()
    model.load()
    # for i in range(0,10):
    #     print(i)
    #     time.sleep(1)
    # print("start predict")

    # img = cv2.imread('capture.png')
    img = cv2.imread('capture.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
