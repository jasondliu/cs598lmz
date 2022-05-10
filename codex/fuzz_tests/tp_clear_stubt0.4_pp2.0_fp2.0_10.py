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
del latefin
gc.collect()
</code>
The problem is that I can't find a way to make this work with a <code>__del__</code> method.  The <code>__del__</code> method is called during the collection of the <code>Cyclic</code> object, which is already being collected, so the <code>__del__</code> method can't create a new reference to the <code>Cyclic</code> object.
I can't find any way to get a reference to the <code>Cyclic</code> object, since it's already being collected.  I can't find any way to make a new reference to the <code>Cyclic</code> object, since it's already being collected.
The only way I can think of to make this work is to make the <code>__del__</code> method create a new reference to the <code>Cyclic</code> object before the <code>Cyclic</code> object is collected.  But I can't think of any way to do that.
I can't even make a reference
