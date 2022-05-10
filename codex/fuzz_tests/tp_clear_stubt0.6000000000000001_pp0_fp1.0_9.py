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
gc.collect()
gc.collect()

# call the method with the weak reference to the instance
func()
</code>
I've done a rough benchmark on CPython, Pypy and Jython.  I've also added an alternate implementation of the weak reference that does not involve <code>__del__</code> at all.  Here are the results:
<code>                                             CPython  Pypy  Jython
del__                                          1.0   6.0  10.0
weakref_with_ref                               1.0   8.0  40.0
weakref_with_ref_no_del                        1.0   1.0   1.0
weakref_with_ref_no_del_no_gc                  1.0   1.0   1.0
</code>
The "del__" version is the original version, the one with "weakref_with_ref" is the one that uses a weak reference to the instance (without <code>__del__</code>), the one with "weakref_with_ref_no_
