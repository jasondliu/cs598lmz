import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
   return 1.0

from multiprocessing.managers import DictProxy, BaseProxy
