import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    class A(object):
        pass
    return A
</code>
and:
<code>c = fun()
</code>
returns <code>TypeError: cannot create 'A' instances</code>

I've tried also <code>ctypes.c_void_p</code> as return type, but that just returns <code>None</code>.
I've read the docs, but I can't find how to make this work.


A:

You need to use <code>PyType_FromSpec</code> in the C function and return the result.
<code>#include &lt;Python.h&gt;

static PyObject*
create_type(void)
{
    static PyType_Slot slots[] = {
        {Py_tp_dealloc, NULL},
        {0, NULL}
    };
    static PyType_Spec spec = {
        .name = "A",
        .basicsize = sizeof(PyObject),
        .itemsize = 0,
        .flags = Py_TPFLAGS_DEFAULT,
        .slots = slots
