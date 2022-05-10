import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import numpy as np
import cv2

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import sys
sys.path.append('../')
from lib.utils import load_image
from lib.utils import draw_image
from lib.utils import draw_image_with_contours
from lib.utils import draw_contours
from lib.utils import draw_contours_and_hulls
from lib.utils import draw_contours_and_hulls_and_defects
from lib.utils import draw_contours_and_hulls_and_defects_and_fingers
from lib.utils import draw_contours_and_hulls_and_defects_and_fingers_and_palm
from lib.utils import draw_contours_and_hulls_and_defects_and_fingers_and_palm_and_fingers_tips
from lib.utils import draw_contours_and
