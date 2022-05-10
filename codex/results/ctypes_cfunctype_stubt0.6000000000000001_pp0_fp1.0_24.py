import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
</code>
This doesn't work because <code>None</code> is not an object.
I'm using Python 2.7.


A:

It's not a good idea to try to return <code>None</code> from a C function.  The C code can't know whether the caller will expect a <code>PyObject</code> or a <code>Py_ssize_t</code> (or whatever other type of C value is needed).  A better strategy is to use the Python <code>c_void_p</code> type, but then you'll need to cast the result to <code>PyObject</code> in order to use it in Python code.  Here's a short example:
<code>#include &lt;Python.h&gt;

PyObject *py_fun()
{
    return (PyObject*)Py_None;
}
</code>
compile this with something like
<code>gcc -o myc.so -shared myc.c -I/usr/include/python2.7 -lpython2.7
</code>
and
