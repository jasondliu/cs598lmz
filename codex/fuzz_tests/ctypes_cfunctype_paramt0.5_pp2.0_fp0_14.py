import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print 'My callback is called with %d and %d' % (a, b)
    return 0

CALLBACK = FUNTYPE(my_callback)
</code>
Then, I want to pass this callback to a C library. The C library is using <code>py_object</code> to receive the callback.
<code>#include &lt;Python.h&gt;
static PyObject *
my_callback(PyObject *self, PyObject *args) {
    PyObject *result = NULL;
    PyObject *temp;

    if (PyArg_ParseTuple(args, "O:my_callback", &amp;temp)) {
        if (!PyCallable_Check(temp)) {
            PyErr_SetString(PyExc_TypeError, "parameter must be callable");
            return NULL;
        }
        Py_XINCREF(temp);
        Py_XDECREF(my_callback);
        my
