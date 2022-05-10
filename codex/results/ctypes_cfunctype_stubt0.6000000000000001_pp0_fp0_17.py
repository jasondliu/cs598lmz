import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ['a', 'b', 'c']

def test_list_of_strings():
    with open('test_list_of_strings.c', 'w') as f:
        f.write("""
        #include <Python.h>
        #include <stdio.h>
        #include <stdlib.h>

        PyObject* fun(void) {
            PyObject* lst = PyList_New(3);
            PyList_SET_ITEM(lst, 0, PyString_FromString("a"));
            PyList_SET_ITEM(lst, 1, PyString_FromString("b"));
            PyList_SET_ITEM(lst, 2, PyString_FromString("c"));
            return lst;
        }

        static PyMethodDef methods[] = {
            {"fun", (PyCFunction)fun, METH_NOARGS, NULL},
            {NULL, NULL, 0, NULL}
        };

        PyMODINIT_FUNC inittest_list_of_strings(void) {
            Py
