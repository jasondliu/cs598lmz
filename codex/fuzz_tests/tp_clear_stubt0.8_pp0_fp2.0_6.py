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
</code>
Calling <code>gc.collect()</code> in a loop should be enough to empty the cyclic trash, but here it doesn't happen. In fact, <code>gc.collect()</code> just removes the cyclic trash attached to <code>func</code>, but leaves the one attached to <code>latefin</code> (causing the assertion to fail).
I have tried to debug the problem, but all I can see is that <code>gc.collect()</code> considers the cyclic trash attached to <code>func</code> to be "uncollectable", while the one attached to <code>latefin</code> is considered "collectable". I have no idea why this would be and I don't even know how to debug this further.
Of course, <code>gc.collect()</code> does its job and empties the cyclic trash after a while. But this is not enough for my program, because the cyclic trash has to be cleared on the fly rather than at some unspecified later point.


A:

I was able
