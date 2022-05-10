import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc, LateFin, Cyclic

gc.collect()
gc.collect()
gc.collect()
gc.threshold(100, 1, 1)

"""#define Py_TRACE_REFS
#define Py_EMBEDDED 0
#include "Python.h"
#include "gcmodule.h"

static PyObject *
gc_collect(PyObject *self, PyObject *args)
{
    PyGC_Collect();
    Py_RETURN_NONE;
}

static PyMethodDef GcMethods[] = {
    {"collect", gc_collect, METH_VARARGS,
     "Invoke the garbage collector"
    },
    {NULL, NULL, 0, NULL}  /* sentinel */
};

static struct PyModuleDef gcmodule = {
    PyModuleDef_HEAD_INIT,
    "gc",
    NULL,
    -1,
    GcMethods
};

PyMODINIT_FUNC
PyInit_gc(void)
{
    return PyModule_Create(&gcmodule);
}
"""
