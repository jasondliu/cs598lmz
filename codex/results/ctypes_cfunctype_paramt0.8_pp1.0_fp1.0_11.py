import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_int)
print 'FUNTYPE:', repr(FUNTYPE)

from ctypes import windll
from ctypes import c_int
from ctypes import c_double
from ctypes import c_void_p
from ctypes import c_char
from ctypes import cast
from ctypes import CFUNCTYPE

from ctypes import Structure
from ctypes import c_long
from ctypes import c_double

#import numpy as np
#import pdb

class Acc_data(Structure):
    _fields_ = [("x", c_double),
                ("y", c_double),
                ("z", c_double)]

class Gyro_data(Structure):
    _fields_ = [("x", c_double),
                ("y", c_double),
                ("z", c_double)]

class Mag_data(Structure):
    _fields_ = [("x", c_double),
                ("y", c_double),
                ("z", c_double)]

class Euler_data(Structure):
   
