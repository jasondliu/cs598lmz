import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle
import glob
import os

from moviepy.editor import VideoFileClip
from IPython.display import HTML

from camera_calibration import calibrate_camera
from perspective_transform import perspective_transform
from lane_detection import detect_lane_pixels, fit_polynomial, measure_curvature_real, draw_lane

# Calibrate camera
calibration_images = glob.glob('./camera_cal/calibration*.jpg')
ret, mtx, dist, rvecs, tvecs = calibrate_camera(calibration_images)

# Perspective transform
src = np.float32([[585, 460], [203, 720], [1127, 720], [695, 460]])
dst = np.float32([[320, 0], [320, 720], [960, 720], [960, 0]])
M = perspective
