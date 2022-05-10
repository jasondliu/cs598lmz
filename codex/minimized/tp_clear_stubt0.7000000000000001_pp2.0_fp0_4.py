import gc, weakref
class LateFin:
    def __del__(self):
        global func
        func = self.ref()
class Cyclic(tuple):
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
print(func())
