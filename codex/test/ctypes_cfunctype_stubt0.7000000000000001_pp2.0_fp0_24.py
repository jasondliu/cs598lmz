import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

from ctypes import *
from ctypes import util
import ctypes.macholib.dyld
name = util.find_library('libc.dylib')
name = str(name)
