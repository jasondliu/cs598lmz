import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

def get_func():
    global func
    return func()


"""
>>> from extension2 import get_func
>>> get_func()
'draw_into'

>>> import sys
>>> get_func().__module__.__path__ is sys.modules["somemodule"].__path__
True

"""

"""
In CPython, the following is output:

   cyclic reference created
   cycle detected

To get that behavior in Jython, comment out the `get_func()` call.

If one runs this test with get_func() commented out, then CoreLinker.setDependencies
would not be called (line 191) and the exception would not be raised.

"""
