import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "in python callback"
    return a + b

my_callback = FUNTYPE(my_callback)

dll = ctypes.CDLL('./libtest.so')
dll.set_callback(my_callback)
dll.test()
</code>
This works fine, but I would like to be able to pass a function with a different signature to the callback.  For example, I would like to be able to pass a function that takes a string and an int.  Is there a way to do this?


A:

You can use a <code>ctypes.c_void_p</code> as the callback argument, and pass a pointer to a Python function object.  The C code can then call the Python function using <code>PyObject_CallFunction</code>.
<code>#include &lt;Python.h&gt;

static PyObject *callback = NULL;

void set_callback(PyObject *cb)
{
    Py_
