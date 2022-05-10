import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello world")
    return b"hello world"
lib = ctypes.cdll.LoadLibrary("./libpyfun.so")
lib.fun = fun
lib.fun()
</code>
In C:
<code>#include &lt;Python.h&gt;
PyObject* fun(){
    Py_Initialize();
    PyRun_SimpleString("print('hello world')");
    Py_Finalize();
    PyObject* pStr = PyUnicode_FromString("hello world");
    return pStr;
}
</code>
But when I call the C function in Python, it throws a segmentation fault.
<code>lib.fun()
</code>
How can I call a Python function in C?


A:

You can't call Python code from C. To do so, you need to use the Python C API.
<code>#include &lt;Python.h&gt;

static PyObject*
hello(PyObject *self, PyObject *args)
{
    Py_RETURN_NONE;
}

static PyMethod
