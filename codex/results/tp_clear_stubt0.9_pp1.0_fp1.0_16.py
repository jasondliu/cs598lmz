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
</code>
<code>func</code> seems to be collected (at least <code>cyclic.__del__</code> raises an AttributeError when accessing <code>latefin.ref</code>), but the refcounts of <code>func</code>, <code>Cyclic</code> and <code>LateFin</code> are all 3.  Worse, CPython sends the <code>func</code> reference count to 6.  
It's not just Python code, C extension can also hold references to the function indefinitely:
<code>#include &lt;Python.h&gt;

PyObject *ref;

PyObject *func(PyObject *self, PyObject *args) {
    Py_INCREF(ref);
    return ref; // even if this is a new reference, it will be collected
    // Py_RETURN_NONE is fine since it's just a const reference
}

PyMethodDef module_methods[] = {
    {"func", func, METH_NOARGS, NULL},
    {"call_
