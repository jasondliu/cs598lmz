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

# This is a bit of a hack, but it's the only way to get the
# reference count of the function object to 1.
del latefin
gc.collect()

# Now we can delete the function object.
del latefin
gc.collect()

# And now we can delete the module object.
del latefin
gc.collect()

# And now we can delete the module dict.
del latefin
gc.collect()

# And now we can delete the module name.
del latefin
gc.collect()

# And now we can delete the module type.
del latefin
gc.collect()

# And now we can delete the module type dict.
del latefin
gc.collect()

# And now we can delete the module type name.
del latefin
gc.collect()

# And now we can delete the module type base.
del latefin
gc.collect()

# And now we can delete the module type base dict.
del latefin
gc.collect()

# And now we can delete the module type base name.
del
