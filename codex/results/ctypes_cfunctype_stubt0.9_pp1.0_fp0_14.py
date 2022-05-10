import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hi")
    return 0
from gi.types import GObjectMeta
#from aiohttp.web_app import Application
#from typing import Constant
from numbers import Integral
from enum import IntEnum
func = fun # type: GObject.ObjectMethod
from ctypes.wintypes import INT

def int_to_bytes(x: INT = 1)->bytes:
    return bytes([x])
