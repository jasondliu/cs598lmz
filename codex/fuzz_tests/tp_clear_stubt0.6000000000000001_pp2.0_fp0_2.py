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
Note that I've changed the code in a few ways to make it more portable.  In particular, I've made the <code>LateFin</code> class use <code>__slots__</code> and I've removed the <code>__dict__</code> of the <code>Cyclic</code> class, since <code>tuple</code> doesn't have one.  (The <code>__dict__</code> was unnecessary in the original version, since they were only using it to store the <code>__module__</code> of the function.)

