import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import cv2
import time
import os
import sys
import shutil
import tensorflow as tf
import threading
import multiprocessing
from multiprocessing import Process, Queue, Pool
from utils import detector_utils as detector_utils
import datetime

frame_processed = 0
score_thresh = 0.2

detection_graph, sess = detector_utils.load_inference_graph()

if __name__ == '__main__':

    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture('../../../../../../home/jess/Downloads/test.mp4')
    start_time = datetime.datetime.now()
    num_frames = 0
    im_width, im_height = (cap.get(3), cap.get(4))
    # max number of hands we want to detect/track
    num_hands_detect =
