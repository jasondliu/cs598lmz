import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return bytes([0x41])
sys.setdlopenflags(sys.getdlopenflags() & ~ctypes.RTLD_GLOBAL)
lib = ctypes.cdll.LoadLibrary(
            self.path, ctypes.RTLD_GLOBAL | ctypes.RTLD_LAZY)
lib.fun = lib.fun
with self.assertRaises(ctypes.ArgumentError) as e:
    lib.fun()
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
ArgumentError: argument 1: <class 'TypeError'>: incorrect type

'''

import ctypes
import sys
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return bytes([0x41])
sys.setdlopenflags(sys.getdlopenflags() & ~ctypes.RTLD_GLOBAL)
lib = ctypes.cdll.LoadLibrary(
            self.path, ctypes.RTLD_GLOBAL | ctypes.RT
