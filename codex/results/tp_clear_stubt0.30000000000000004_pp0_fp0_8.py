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

# The following is a test for a bug in the implementation of weakrefs
# for function objects.  The bug was that the weakref was not cleared
# when the function object was deleted.

import weakref

def f():
    pass

def g():
    f()

wr = weakref.ref(f)

del f
gc.collect()

try:
    wr()
except ReferenceError:
    pass
else:
    raise Exception("weakref not cleared")

del wr

# The following is a test for a bug in the implementation of weakrefs
# for function objects.  The bug was that the weakref was not cleared
# when the function object was deleted.

import weakref

def f():
    pass

def g():
    f()

wr = weakref.ref(f)

del f
gc.collect()

try:
    wr()
except ReferenceError:
    pass
else:
    raise Exception("weakref not cleared")

del wr

# The following is a test for a bug
