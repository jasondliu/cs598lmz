import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 123

fun()

ctypes.pythonapi.PyObject_SetAttrString(ctypes.py_object(fun),
                                        "__call__",
                                        fun)

fun()
</code>
This is on CPython 3.3, CPython 2.7 and pypy 1.9.

