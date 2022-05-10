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
</code>
This fails when it is run as is but succeeds if <code>LateFin</code> is no longer the class of <code>latefin</code>. It was previously <code>__dealloc__</code> that was problematic, now it is <code>__dict__</code>.
Am I going to run into more of these inconsistencies, or am I guaranteed to be able to <code>func.func_globals</code> or <code>func.__module__</code> if <code>func</code> is a bound method without affecting order of destruction?


A:

To determine if the global <code>func</code> is no longer accessible, you can use <code>gc.get_referents()</code>. I'm not sure if you can cleanly write a <code>__del__</code> to do this that won't cause the bug to trigger again.
<code>import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.
