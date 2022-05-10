import ctypes
ctypes.cast(0, ctypes.py_object)

# from libc.stdlib cimport malloc, free
# from libc.stdint cimport uintptr_t
# from cpython.ref cimport PyObject
#
# cdef uintptr_t ptr = <uintptr_t>malloc(<size_t>sizeof(PyObject))
# cdef PyObject *obj = <PyObject *>ptr
#
# free(<void *>ptr)

# from cpython.ref cimport PyObject
# from cpython.ref cimport Py_INCREF, Py_DECREF
# from cpython.ref cimport Py_RETURN_NONE
#
# cdef class MyClass:
#     cdef PyObject *obj
#
#     def __cinit__(self, obj):
#         self.obj = obj
#         Py_INCREF(self.obj)
#
#     def __dealloc__(self):
#         Py_DECREF(self.obj)
#
#     def __repr__(self):
#         return "<MyClass object>"
