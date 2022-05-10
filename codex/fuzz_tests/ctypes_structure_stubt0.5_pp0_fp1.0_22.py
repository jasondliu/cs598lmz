import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class X(object):
    def __init__(self):
        self.s = S()

x = X()
x.s.x = 42

# This creates a new S instance, instead of sharing the one from x.s.
# This is because x.s.x is a ctypes.c_int, not a ctypes.Structure.
y = ctypes.cast(x.s.x, ctypes.POINTER(S))

print x.s.x, y.contents.x
print x.s.x is y.contents
</code>

