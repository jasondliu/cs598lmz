import ctypes
ctypes.cast(0, ctypes.py_object).value

# this line will crash your python install
# ctypes.cast("s", ctypes.py_object).value

PyObject_HEAD = [
    ('ob_refcnt', ctypes.c_size_t),
    ('ob_type', ctypes.c_void_p),
]

class PyIntObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('ob_ival', ctypes.c_long)
    ]

class PyTypeObject(ctypes.Structure):
    _fields_ = PyObject_HEAD + [
        ('tp_name', ctypes.c_char_p)
    ]

print(PyObject_HEAD)
print(PyTypeObject)
print(PyIntObject)

obj = ctypes.cast(id(1), ctypes.POINTER(PyIntObject))
print(obj.contents.ob_ival)
print(hex(id(int)))
print(PyTypeObject.from_address(id(int)).tp_name)
print
