import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
print(fun()([]))

$ python2 ctypes_python_return.py
42
$ python3 ctypes_python_return.py
42
```

```
$ cat ctypes_pycall.c
#include <Python.h>
int main() {
    Py_Initialize();
    printf("%ld\n", PyCallable_Check(PyInt_FromLong(42)));
    printf("%ld\n", PyCallable_Check(PyLong_FromLong(42)));
    printf("%ld\n", PyCallable_Check(PyUnicode_DecodeFSDefault("42")));
    printf("%ld\n", PyCallable_Check(PyFloat_FromDouble(42)));
    printf("%ld\n", PyCallable_Check(PyBytes_FromString("42")));
    printf("%ld\n", PyCallable_Check(PyList_New(0)));
    printf("%ld\n", PyCallable_Check(PyTuple_New(0)));
    printf("%ld\
