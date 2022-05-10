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
del func, cyc, latefin

for step in range(2):
    gc.collect()
    assert func() is None, func.__module__
"""

tests = [
    ("""
class C: 'abc' in globals()
""", {}, {'a' : 'abc'}, ""),
    ("bar in globals()", {}, {'bar': 42}, ""),
    # nice loop
    ("""
def f():
    while 1:
        try:
            return 1
        finally:
            gc.collect()
            if f():
                continue
""", {'f': f}, {}, ""),
    # test memory leakage
    ("""
import weakref as w

class C: pass
class E: pass

for i in xrange(1000):
    c = C()
    w.ref(c)
    del c
""", globals(), {}, ""),
    # recursive calls
    ("""
import weakref as w

def foo():
    remember = {}

