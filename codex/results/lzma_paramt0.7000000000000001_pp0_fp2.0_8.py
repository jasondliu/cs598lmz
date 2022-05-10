from lzma import LZMADecompressor
LZMADecompressor().decompress(requests.get('https://github.com/pravj/face-recognition/blob/master/models/face_landmark_68_model.dat?raw=true').content)

#----------------------------------------

import cv2
import dlib
import numpy as np

PREDICTOR_PATH = "face_landmark_68_model.dat"

predictor = dlib.shape_predictor(PREDICTOR_PATH)

detector = dlib.get_frontal_face_detector()

lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

feature_params = dict( maxCorners = 500,
                       qualityLevel = 0.1,
                       minDistance = 7,
                       blockSize = 7 )

class TooManyFaces(Exception):
    pass

class NoFaces(Exception):

