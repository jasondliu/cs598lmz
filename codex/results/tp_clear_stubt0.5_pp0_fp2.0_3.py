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

try:
    latefin.ref()
except TypeError:
    print('SKIP')
    raise SystemExit

# the bug is that the __del__ method of 'latefin' is called twice
# the first time, it sets 'func' to the weakref to 'cyc[0]'
# the second time, it tries to set 'func' to the weakref to 'cyc[0]' again
# but 'cyc[0]' has been deleted, so the weakref returns None
# and the second time, 'func' is set to None
# the result is that 'func' is None, even though it was supposed to be set
# to the weakref to the function
print(latefin.ref())
