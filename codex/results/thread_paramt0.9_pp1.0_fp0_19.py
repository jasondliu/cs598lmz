import sys, threading
threading.Thread(target=lambda: sys.stderr.write('\x1b[2J\x1b[H'),daemon=True).start()

import cv2
import matplotlib.pyplot as plt
import numpy as np
import traceback

import detector
import find
import model
import scn
import util

# 読み込む画像番号
input_img = 2
# 検出するオブジェクトの半径の平均[m]
object_radius_mean = 0.05
# キャリブレーションの番号
calib_img = 1
# キャリブレーションの物体間距離[m]
distance_calib = 0.53

# カメラのキャリブレーション
# c_mat, d_vec = util.calibration(calib_img)
c_mat = np.array([[307.901320
