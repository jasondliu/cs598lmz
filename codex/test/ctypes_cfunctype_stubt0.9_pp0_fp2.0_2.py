import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return 0
import numpy
a = numpy.zeros(2)
fun()
