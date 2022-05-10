import ctypes
# Test ctypes.CFUNCTYPE

# In:
def f(x):
    return x + 1

# Out:
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(f)

# In:
f(1)

# Out:
2
# Test ctypes.cast

# In:
a = numpy.arange(10)

# Out:
# In:
ctypes.cast(a.ctypes.data, ctypes.POINTER(ctypes.c_int))[0] == a[0]

# Out:
True
# Test ctypes.pointer

# In:
class Foo(object):
    def __init__(self, x):
        self.x = x
    def add_to(self, a):
        a += self.x

# Out:
# In:
foo = Foo(1)

# Out:
# In:
a = numpy.arange(10)

# Out:
# In:
p = ctypes.pointer(foo)

# Out:

