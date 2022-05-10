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

assert latefin.ref() is None
del latefin

"""

test_autogc2 = """

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

def func():
    global cyc
    cyc = tuple.__new__(Cyclic, (func, latefin))
    func.__module__ = cyc

latefin = LateFin()
func()
del func, cyc
gc.collect()

assert latefin.ref is not None
assert latefin.ref() is None
del latefin

"""

test_gctrans = """

import gc

class C(object):
    def __init__(self, loop):
       
