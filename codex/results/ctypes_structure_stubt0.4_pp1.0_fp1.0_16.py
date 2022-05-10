import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class D(S):
    x = ctypes.c_short

ctypes.sizeof(D)
</code>
This code prints <code>4</code> on my machine, but I would expect it to print <code>2</code>.
Is this a bug in ctypes?

