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

# if func is not None:
#     print("Warning: failed to trigger func.__del__")
# else:
#     print("func.__del__ triggered")

# if latefin is not None:
#     print("Warning: failed to trigger latefin.__del__")
# else:
#     print("latefin.__del__ triggered")
