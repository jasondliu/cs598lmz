import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)
FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), './python_binding/'))
from cpp_transformation import *
import numpy as np
from numpy.ctypeslib import as_ctypes, ndpointer
import cv2

def check_status(status):
    if status != 0:
        raise IOError("Transformation failed (status = %d)" % status)

class PerspectiveTransformation:
    def __init__(self, config):
        self.config = config
        self.transformation = None
        self.w, self.h = self.config.image_size
        self.transformation = create_perspective_transformation(self.w, self.h, self.config.corners, self.config.
