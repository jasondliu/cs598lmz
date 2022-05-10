import threading
threading.stack_size(67108864)

import sys
sys.path.append('../')
from utils import *

import os
import glob

import cv2
import dlib
import numpy as np
from scipy.spatial import distance

from keras.models import load_model

from tqdm import tqdm

# https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/
def get_face_landmarks(img):
    """
    Finds the face image landmarks.
    Returns the list of landmark points, or None if no face was found.
    """
    face_detector = dlib.get_frontal_face_detector()
    face_pose_predictor = dlib.shape_predictor('../models/shape_predictor_68_face_landmarks.dat')

    # 1) Check face detection
    detected_faces = face_detector(img, 1)
    if len(detected_faces) != 1:
        return
