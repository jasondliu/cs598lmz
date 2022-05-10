import gc, weakref
#from gpr import GPR, GPRf
import numpy as np
from scipy.interpolate import interp1d

from gpr.gp_regression import GPR
from gpr.utils.kernels import SE_Kernel
from gpr.utils.kernels import SE_Kernel_RBF

#from gpr.gpr_cuda import gpr_cuda
import os

#from umpy.utils import gauss_weighted_sum, gauss_weighted_max, gauss_weighted_mean
#from umpy.utils import gauss_weighted_sum
from utils import gauss_weighted_sum
import os.path

import sys
import time
sys.path.append('/home/ayagoz/conveyor_belt/document_recognition/document_recognition/')

from document_recognition.keypoints_algorithms import SIFT
#from document_recognition.keypoints_algorithms import SIFT_GPU
#sift_gpu = SIFT_GPU()
import cv2

