fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #3424: cffi objects should not be able to be subclasses
import cffi
class B(cffi.FFI):
    pass
try:
    class C(object):
        __metaclass__ = type(cffi.FFI)
except TypeError:
    pass
else:
    assert 0, "should not be able to create a subclass of cffi.FFI"

# Issue #3426: do not crash when a __del__ function in CFFI calls back
# Python and raises an exception
import cffi
ffi = cffi.FFI()
ffi.cdef("""
    typedef struct {
        PyObject_HEAD
    } Spam;
""")
C = ffi.verify("""
    typedef struct {
        PyObject_HEAD
    } Spam;
    static void Spam_dealloc(Spam *self) {
        PyErr_SetString(PyExc_ValueError, "boo!");
        Py_DECREF(self);
    }
