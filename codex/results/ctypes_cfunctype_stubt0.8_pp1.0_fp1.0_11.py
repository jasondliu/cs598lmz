import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0
</code>
However, this gives:
<code>Segmentation fault (core dumped)
</code>
How do I implement a function that returns an <code>object</code> from C?


A:

In C, you have
<code>PyObject* fun(void)
</code>
and, in Python,
<code>@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 0
</code>
To call the function in C, you could do
<code>PyObject* o = fun();
Py_INCREF(o);
</code>
and then use <code>o</code> somewhere, finally calling <code>Py_DECREF</code> to tell Python that you're done with <code>o</code>.

