import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32m' + (' ' * 20) + '\r')).start()
#sys.stdout.write('\x1b[1;32m' + (' ' * 20) + '\r')
#sys.stdout.flush()

import cv2
import argparse
import numpy as np
import os.path
import sys
import time
from threading import Thread

import util
from input_feeder import InputFeeder
from mouse_controller import MouseController
from face_detection import FaceDetection
from head_pose_estimation import HeadPoseEstimation
from facial_landmarks_detection import FacialLandmarksDetection
from gaze_estimation import GazeEstimation
from mouse_controller import MouseController
from argparse import ArgumentParser
from pathlib import Path
from openvino.inference_engine import IENetwork, IECore


def main(args):
    start_model_load_time = time.time()
    face_detection = FaceDetection(args.fd_model)

