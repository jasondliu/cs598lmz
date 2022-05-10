import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64(3)
    y = ctypes.c_int64(4)


s = S()

s.x = 2 # &lt;- works
s.y = 2 # &lt;- error: 'c_longlong' object does not support assignment
