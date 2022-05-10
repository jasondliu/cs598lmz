import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

import time

import pyaudio
import wave

import scipy.io.wavfile as wav

import os

import math

import random

import csv

import pickle

import copy

import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D

from tensorflow.keras.callbacks import TensorBoard

import pickle
import time

import cv2

import pygame

import pygame.camera

import pygame.surfarray

import pygame.image

import pygame.transform

import pygame.gfxdraw

import pygame
