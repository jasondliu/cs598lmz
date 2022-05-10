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

# This is necessary to trigger the bug.
del latefin


import builtins
import gc

def f():
    class LateFin:
        __slots__ = ()
        def __del__(self):
            global x
            x = 1
    global x
    x = 2
    builtins.LateFin = LateFin
    del LateFin
    gc.collect()
    return x

assert f() == 1


import builtins
import gc

class MyInt(int):
    __slots__ = ()
    def __del__(self):
        global x
        x = 1

def f():
    global x
    x = 2
    int.__new__ = MyInt
    del MyInt
    gc.collect()
    return x

assert f() == 1


import builtins, gc
from io import BytesIO
import _io

class MyBytesIO(BytesIO):
    __slots__ = ()
    def __del__(self):
        global x
        x = 1
