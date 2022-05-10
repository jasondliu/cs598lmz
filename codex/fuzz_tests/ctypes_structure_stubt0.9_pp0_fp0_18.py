import ctypes

class S(ctypes.Structure):
    x = 1
    _pack_ = 1

S.x = ctypes.c_ulonglong(10)
</code>
That code also works if you supply an initializer to S.x and assign a new value to S.x, but that's not very interesting.

