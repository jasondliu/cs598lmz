import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

import cv2
import numpy as np
import math
import dlib
import imutils
import time
import pyautogui

from scipy.spatial import distance as dist
from imutils import face_utils
from pygame import mixer

mixer.init()

EYE_AR_THRESH = 0.22
EYE_AR_CONSEC_FRAMES = 2

COUNTER = 0
TOTAL = 0

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def sound_alarm(path):
    mixer.music.load(path)
    mixer.music.play()

def midpoint(p1, p2):
    return int((p
