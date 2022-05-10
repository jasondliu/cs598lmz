import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(int)
    _fields_ = [("x", ctypes.POINTER(int))]

s = S()

s.x = ctypes.cast(ctypes.c_void_p(0x41), ctypes.POINTER(ctypes.c_int))
s.x = ctypes.POINTER(ctypes.c_int)(0x41)
s.x = 0x41
s.x = ctypes.c_int(0x41)
s.x = ctypes.cast(ctypes.c_void_p(0x41), ctypes.POINTER(ctypes.c_int))
s.x = ctypes.cast(ctypes.c_void_p(0x41), ctypes.c_int)
</code>
Both the last two work.
However, now I've added <code>typedef struct A {int x;} A;</code> and changed <code>ctypes.c_int</code> to <code>A</code>
Only the last one works, the following gives <code>TypeError:
