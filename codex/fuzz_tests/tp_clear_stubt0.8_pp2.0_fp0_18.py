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
print(latefin.ref() is None)
del latefin
gc.collect()

class MySlotted(tuple):
    pass

a = MySlotted((1,2,3))

# at this point the tuple is living in the __dict__ of MySlotted
# and thus not visible to the GC (which looks at type slots)
for i in range(100):
    s = MySlotted()

gc.collect()

a[1] = 2

# at this point the tuple is moved to the steady set,
# and there is a cycle between the tuple and the object
# reference in the dict, but we don't crash this time
del a
