import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p
    #ctypes.POINTER(ctypes.c_void_p)
print S
ctypes.cast
from ctypes import *
from ctypes import CDLL, POINTER, Structure
import ctypes.wintypes
from ctypes.wintypes import *


class tagRECT(ctypes.Structure):
    _fields = [
        ('left', c_int),
        ('top', c_int),
        ('right', c_int),
        ('bottom', c_int)]


RECT = tagRECT
LPRECT = POINTER(RECT)
LPPOINT = POINTER(tagPOINT)
tagPOINT = POINTER(ctypes.wintypes.LONG)
#LPPOINT = POINTER(POINT)


class tagPOINT(Structure):
    _fields_ = [('x', c_long),
                ('y', c_long)]


class tagMSG(Structure):
    _fields_ = [('HWnd', c_void_p),
                ('message', c_uint),
               
