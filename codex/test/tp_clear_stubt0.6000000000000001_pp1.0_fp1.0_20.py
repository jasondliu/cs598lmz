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

# Clear the reference to LateFin and force a collection
# to trigger the creation of a weakref to it.
latefin = None
for i in range(10):
    gc.collect()

# The call to LateFin.__del__ will create a reference to func
# which will be used in the creation of the weakref.
del latefin

# Clear the reference to LateFin and force a collection.
# This will trigger the call to LateFin.__del__.
gc.collect()

# The weakref to func is now in the weakref list.
# Clear the reference to func and force a collection.
# This will trigger the call to the weakref's callback.
func = None
gc.collect()

# func is now dead, but the weakref to it is still alive.
print(weakref.getweakrefcount(func))
print(weakref.getweakrefs(func))

# Clear the reference to func and force a collection.
# This will trigger the call to the weakref's __del__.
# The __del__ will try to call func.
#
