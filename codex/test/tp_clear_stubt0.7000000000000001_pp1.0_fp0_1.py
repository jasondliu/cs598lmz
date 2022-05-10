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
assert not hasattr(latefin, 'ref')



# Make sure we can call __del__ methods on weakrefs even if they are
# in a cycle.

def callback(ref):
    assert ref() is None
    global callback_called
    callback_called = True

class A:
    def __del__(self):
        B().b = self

class B:
    def __del__(self):
        weakref.ref(self.b, callback)

b = B()
b.b = A()
del b
gc.collect()
assert callback_called



class A:
    def __del__(self):
        global a
        a = None
        global A_deleted
        A_deleted = True
        assert a is None

a = A()

global a_ref
a_ref = weakref.ref(a)

del a

gc.collect()

assert A_deleted
assert a_ref() is None



