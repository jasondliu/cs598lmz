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
assert func() is None, 'weakref callback not called'
"""

def test_del_weakref_callback():
    def callback(x):
        global X
        X = x
    x = Test()
    x.ref = weakref.ref(x, callback)
    x.data = [1,2,3]
    del x
    gc.collect()
    assert X is None, 'weakref callback not called'

def test_weakref_callback_doesnt_keep_alive():
    class X:
        pass
    a = X()
    b = X()
    b.a = a
    a.b = b
    wr = weakref.ref(a)
    del a, b
    gc.collect()
    assert wr() is None, 'object not dead'

def test_weakref_callback_doesnt_keep_alive_subsubclass():
    class X:
        pass
    class Y(X):
        pass
    class Z(Y):
        pass
    x = X()

