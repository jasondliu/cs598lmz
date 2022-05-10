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
del func, cyc, LateFin, Cyclic
gc.collect()
_ = chr(latefin)
"""

def test_cpython_leak_call_finalizer(space):
    space.execute(code, raise_what="exceptions.MemoryError")

code = """\
class Foo:
    i = 0

def close(i):
    def f(space):
        space.buildclass(Foo, None, None)
        space.callmethod(space.int(i), '__del__', ())
    return f

import os, sys

for i in range(60):
    sys.tracefunc = close(i)
    os.write(sys.stdout.fileno(), b"x" * 1024)
"""

def test_cpython_bug_3469275(space):
    space.execute(code)

code = """\
class ExtraAttributeFinalizer:
    def __del__(self):
        self.attr = 1

delattr(ExtraAttributeFinalizer(), 'non-existent')
"""

def test_cpython_bug_34
