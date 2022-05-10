import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print 'from C'
    return 10
    
print fun()
#from ctypes import *
from ctypes import *

libc = cdll.LoadLibrary("E:/python/ProgramWork/PythonBasic/Python27/DLL/add.dll")
mydll = libc.add
mydll.restype=c_char_p
print mydll(1, 2)
