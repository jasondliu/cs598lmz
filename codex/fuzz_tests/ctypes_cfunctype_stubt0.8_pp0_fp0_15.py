import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "test"
</code>
In Cython:
<code>FUNTYPE = CFUNCTYPE(py_object)
@FUNTYPE
def fun():
    return "test"
</code>
This is C++ (not Cython):
<code>PyObject* fun() {
    return PyBytes_FromString("test");
}
</code>
I'd like to write the same example in Cython, but I can't find the Cython equivalent of <code>PyBytes_FromString</code> in the Cython documentation.


A:

The Cython equivalent of <code>PyBytes_FromString</code> is <code>bytes("test")</code>.

