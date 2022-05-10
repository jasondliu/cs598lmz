import ctypes
ctypes.cast(24, ctypes.py_object)

ctypes.cast(24, ctypes.c_void_p)


class test_cast(object):
        
    def __repr__(self):
        return "cast"

print hex(ctypes.addressof(ctypes.py_object(test_cast())))
print hex(id(test_cast()))

print test_cast()
print ctypes.cast(id(test_cast()), ctypes.py_object)
print ctypes.cast(id(test_cast()), ctypes.py_object).value

print ctypes.cast(id(test_cast()), ctypes.c_void_p).value

# what I want, in pseudo code:

# in C:
#   typedef struct PyObject {
#       Py_ssize_t ob_refcnt;
#       struct _typeobject *ob_type;
#   } PyObject;

#   typedef PyObject *(*PyObject_Cast)(PyObject *op, PyObject *type);

# in Python:
