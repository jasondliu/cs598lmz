import ctypes
ctypes.cast(0, ctypes.py_object)

# prints "<class 'int'>"
print(type(ctypes.cast(0, ctypes.py_object)))

# raises TypeError: expected LP_PyObject instance instead of LP_int instance
ctypes.cast(0, ctypes.py_object).value

# process finished with exit code 1
```

Note that this is due to the fact that `ctypes.cast(0, ctypes.py_object)` is **not** a "regular" Python object, even if it is of type `object`.

### Python C API

The Python C API allows you to do many things that we can't do in "regular" Python code, including:

- calling Python internals (e.g. `PyObject_IsTrue`)
- manipulating Python objects (e.g. `PyInt_FromLong`)
- creating new Python types (e.g. `PyType_Type`)

There are two ways to use the Python C API:

- **from Python**: by wrapping the C API with Cython, CFFI, or
