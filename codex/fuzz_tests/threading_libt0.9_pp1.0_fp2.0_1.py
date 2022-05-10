import threading
threading.stack_size(2**27)
import sys
import socket
import datetime
import time
import json
import os
import scipy.io
import scipy.misc
import numpy as np
import dlib
import cv2
import pylab as plt

detector = dlib.get_frontal_face_detector()
face_model = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")

def cos_dis(face1, face2):
    return np.sum(np.multiply(face1, face2))

def calcul_dist(img1_feats, img2_feats):
    final_dist = 0
    for feat1, feat2 in zip(img1_feats, img2_feats):
        final_dist += cos_dis(feat1, feat2)
    return final_dist / len(img1_feats)

compare_results_dist = 0.4
compare_results_num = 5

