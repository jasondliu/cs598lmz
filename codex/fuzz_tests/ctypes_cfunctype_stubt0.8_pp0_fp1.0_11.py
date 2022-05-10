import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1, 2, 3)
fun()()

@FUNTYPE
def fgen():
    yield 1
    yield 2
    yield 3
fgen()()
</code>
I'm using <code>CFUNCTYPE</code> in order to let CPython automatically free the allocated memory, I don't want to work with <code>Py_TPFLAGS_HAVE_GC</code> and <code>Py_TPFLAGS_HEAPTYPE</code>, also I don't want to call <code>Py_INCREF</code> and <code>Py_DECREF</code> because I don't like working with reference counts.
I'm not a CPython developer, but I think this should work like this.

