import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, str)

@FUNTYPE
def callback(s):
    print "got", s
    return len(s)

lib = ctypes.CDLL("test_funptr.so")

lib.my_cb(callback)
