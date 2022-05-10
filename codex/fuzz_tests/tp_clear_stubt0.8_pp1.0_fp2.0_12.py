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
del func, cyc, latefin
gc.collect()
gc.collect()
</code>
It shows the behavior of Python 3.1 - 3.3 but not 3.4.  I can easily reproduce the behavior using <code>Cython</code> but as much as possible I'd like to avoid it unless I have to; I have to handle many possible cases.  I know why this happens, but I haven't found any way to find out about the finalizer without creating a new reference cycle.  If there is one its probably something I'm missing in the C API.
EDIT: In Python 2.6.6 the crash only occurs when a <code>func_code</code> object is freed so I've modified it slightly to fit.  Its also worth noting that Python 2.6.6 and older versions of Python 3.x also crash if <code>cyc</code> is freed after the finalization of <code>latefin</code>.  This is also reproduced with <code>Cython</code>.  The <code>tuple</code> subclass is just an attempt to limit the objects that can be cycled to gc.
EDIT 2: It is possible to
