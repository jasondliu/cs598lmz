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

# Exercise the update_raw_weakrefs() function in the cycle
# detector.
x = 42
y = [x]
x = weakref.ref(y)
del x, y
gc.collect()

if func is not None:
    print("warning: __del__ was run too early (-X does not help)")
else:
    print("ok.")
