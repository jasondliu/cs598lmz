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

# now, the latefin object is in a cycle, but holds
# a weakref to itself.  So it should be collected
# and the callback triggered.

print (latefin.__class__, latefin.ref)
assert latefin.__class__ is LateFin
assert latefin.ref() is func
print (func.__class__, func.__module__)
assert func.__class__ is types.FunctionType
assert func.__module__ is cyc
print (cyc.__class__, cyc[1].ref())
assert cyc.__class__ is Cyclic
assert cyc[1].ref() is cyc

# Now, we remove the cycle and make sure it gets collected
del cyc
gc.collect()

print (func.__class__, func.__module__)
assert func.__class__ is types.FunctionType
assert func.__module__ is None
print (latefin.__class__, latefin.ref)
assert latefin.__class__ is None
assert latefin.ref is None

# Check it
