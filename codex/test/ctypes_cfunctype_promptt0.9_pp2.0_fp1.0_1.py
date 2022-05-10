import ctypes
# Test ctypes.CFUNCTYPE() for a callback for which the generator
# expects the self argument (as a weak reference)
import ctypes

def empty():
    pass

selfval = object()
def g(cond, value=None):
    if cond:
        yield value

def g2(cond):
    if cond:
        yield 42


