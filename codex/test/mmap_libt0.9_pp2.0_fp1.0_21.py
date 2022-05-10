import mmap
import re
import subprocess
import random
import time
import win32gui
import pyautogui as pag
import pyperclip
import pywinauto as pwa
import tensorflow.compat.v1 as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

tf.disable_v2_behavior()

def clipping(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    y = int(gray.shape[0] / 2)
    x = int(gray.shape[1] / 2)
    temporal = []
    while True:
        temporal.append(gray[y][x])
        if temporal[-1] > 15 and temporal[-2] > 15 and temporal[-3] > 15:
            break
        y += 1
        x += 1
    value = y % 5

    return gray[value:, 5 * value:]

