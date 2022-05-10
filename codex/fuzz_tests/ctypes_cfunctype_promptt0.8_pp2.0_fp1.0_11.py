import ctypes
# Test ctypes.CFUNCTYPE
import sys

#dll = ctypes.CDLL("./test.dll")
dll = ctypes.CDLL("./libtest.so")

#dll.launch_thread.argtypes = [ctypes.c_int32]
dll.launch_thread.restype = ctypes.c_int32
dll.launch_thread.argtypes = [ctypes.POINTER(ctypes.c_int32)]

def callback(i):
    print "callback function: ", i
    return 0

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)

cmdfunc = CMPFUNC(callback)

#i = ctypes.c_int32()

#i = dll.launch_thread(cmdfunc)
i = dll.launch_thread(ctypes.byref(cmdfunc))

# http://docs.python.org/2/library/ctypes.html#functions-and-methods
# http://stackoverflow.com/questions/1265
