import weakref
# Test weakref.ref(), weakref.proxy() and weakref.getweakrefcount()
import gc

class A:
    pass

def f(x):
    return id(x)

