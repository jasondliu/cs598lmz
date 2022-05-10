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


for gen in [lambda self: g(False),
            lambda self: g(False, selfval),
            lambda self: g(True),
            lambda self: g(True, selfval),
            lambda self: g2(False),
            lambda self: g2(True),
            lambda self: (yield 42),
            lambda self: ()
            ]:
    try:
        runcallback = ctypes.CFUNCTYPE(ctypes.py_object)(gen)
        runcallback(selfval)
    except RuntimeError:
        import traceback
        print "callback %s failed" % gen
     
