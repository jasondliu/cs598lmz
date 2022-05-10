import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    """This function is called from C."""
    return [1, 2, 3]

lib = ctypes.CDLL(__file__.rstrip("c"))
lib.set_fun(fun)
lib.do_stuff()
</code>
The C code:
<code>#include "Python.h"

static PyObject *(*fun)(void) = NULL;

int
do_stuff(void)
{
    PyObject *result = (*fun)();
    return PyList_Check(result);
}

void
set_fun(PyObject *(*f)(void))
{
    fun = f;
}

static PyMethodDef methods[] = {
    { "do_stuff", (PyCFunction)do_stuff, METH_NOARGS, NULL },
    { "set_fun", (PyCFunction)set_fun, METH_VARARGS, NULL },
    { NULL, NULL, 0, NULL }
};

static PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "module",
    NULL,
