import threading
threading.stack_size(2**27)

import pyglet
from pyglet.window import key
import cocos
from cocos.director import director
from cocos.actions import *
from cocos.layer import *
import cocos.collision_model as cm
import cocos.euclid as eu
import cocos.actions as ac

import random
import math
import sys
import time

import pygame
from pygame.locals import *

import numpy as np
import skimage
import skimage.transform
import skimage.color
import skimage.io

import tensorflow as tf

#import tensorflow.contrib.slim as slim

import cv2
import os

#from tensorflow.python import debug as tf_debug

import shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pydot
import graphviz

import re
import json

from datetime import datetime

import keras
from keras.models import Sequential
