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

# call the bound method via a different object
print(latefin.ref().__module__)

print()

# This is to demonstrate the bug in 3.2.3.
# It should be possible to collect _a_, but not _b_.
#
# It should also be possible to collect _b_, but not _a_.
class A:
    def __del__(self):
        try:
            self.b.__del__()
        except:
            pass

class B:
    def __del__(self):
        try:
            self.a.__del__()
        except:
            pass

a = A()
b = B()
a.b = b
b.a = a

del a, b
gc.collect()
