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

# This used to crash
del latefin
</code>
This is what I think is happening:

<code>cyc</code> is deleted, which calls <code>Cyclic.__del__</code>.
<code>Cyclic.__del__</code> then sets <code>latefin.ref</code> to a weakref to <code>func</code>.
This makes <code>func</code> eligible for garbage collection.
<code>func</code> is deleted, which calls <code>LateFin.__del__</code>.
<code>LateFin.__del__</code> then tries to dereference <code>latefin.ref</code> (which was a weakref to <code>func</code>).
<code>func</code> was already deleted, so <code>LateFin.__del__</code> is trying to dereference a dangling pointer.

I've tried to make the code in this question as minimal as possible, but I've left out some details that I think are irrelevant to the problem.  If you think I've omitted something
