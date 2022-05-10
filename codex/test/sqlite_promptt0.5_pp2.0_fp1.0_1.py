import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")

# import cv2
# import numpy as np
# import time

# from matplotlib import pyplot as plt

# import argparse

# parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
#                                               OpenCV. You can process both videos and images.')
# parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
# parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
# args = parser.parse_args()

# if args.algo == 'MOG2':
#     backSub = cv2.createBackgroundSubtractorMOG2()
# else:
#     backSub = cv2.createBackgroundSubtractorKNN()
# capture = cv2.VideoCapture(args.input)
# if not capture.isOpened:
#     print('Unable
