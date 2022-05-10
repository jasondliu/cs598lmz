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
print(latefin.ref.__module__)
</code>
This code is not meant to be useful. It's a minimal reproducer for the problem. The output is
<code>&lt;module '__main__' (built-in)&gt;
</code>
Even though <code>func</code> was deleted, the <code>__module__</code> attribute is still set.
The documentation for <code>weakref.ref</code> says that the attribute <code>__module__</code> is set, but I don't know why.
Is this a bug? Is it possible to get around this, and if so, how?


A:

I found a solution to this problem by using <code>ctypes</code> to call the <code>Py_DECREF</code> function.
<code>import ctypes, weakref

def test():
    Py_DECREF = ctypes.pythonapi.Py_DECREF
    Py_DECREF.argtypes = (ctypes.py_object,)
    Py_DECREF.restype = None
