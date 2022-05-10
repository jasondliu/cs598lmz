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

import gc, weakref

class X:
    __slots__ = ()
    def __del__(self):
        print("d")

class A:
    __slots__ = ("x",)

class B:
    __slots__ = ("a",)

class C:
    __slots__ = ("b",)

class D:
    __slots__ = ("c",)

class E:
    __slots__ = ("d",)

class F:
    __slots__ = ("e",)

class G:
    __slots__ = ("f",)

class H:
    __slots__ = ("g",)

class I:
    __slots__ = ("h",)

class J:
    __slots__ = ("i",)

class K:
    __slots__ = ("j",)

class L:
    __slots__ = ("k",)
