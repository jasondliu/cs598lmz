import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(ctypes.c_int)
s = S()
s.x = ctypes.pointer(ctypes.c_int())

def f(p):
    p = ctypes.cast(ctypes.pointer(ctypes.c_int()), ctypes.c_void_p)
&gt;&gt;&gt; ctypes.cast(ctypes.pointer(ctypes.c_int()), ctypes.c_void_p)
c_void_p(22778720)
&gt;&gt;&gt; ctypes.cast(ctypes.pointer(ctypes.c_int()), ctypes.c_void_p).value
22778720
</code>

