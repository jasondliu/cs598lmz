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
assert not hasattr(latefin, 'ref')

# Test a very specific case of a bug:
#  - __del__ is invoked at the end of a loop
#  - __del__ calls a function
#  - function calls a function
#  - function being called is removed from the module
# This particular bug caused a "frame stack underflow"
# in the frame stack unwinder, because the module
# was being cleared and the top frame's f_code was
# being cleared too.

def f():
    pass

def g():
    f()

def h():
    for i in range(10):
        g()
    del f

