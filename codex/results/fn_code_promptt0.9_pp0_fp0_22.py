fn = lambda: None
# Test fn.__code__
# cpdef test_attr_callability(fn):
#     cdef int rc
#     rc = PyObject_HasAttr(fn, "__module__")
#     if rc == 1:
#         PyErr_Clear()
#         return 1
#     elif rc == 0:
#         PyErr_Clear()
#         return 0
#     else:
#         PyErr_Format(PyExc_ValueError, "Invalid return code")
#         return -1
# Test fn.__code__.co_name == fnn.__code__.co_name
# cpdef tf_get_co_name(fn):
#     cdef int rc
#     cdef PyObject* uni
#     rc = PyObject_HasAttr(fn, "__module__")
#     if rc == 1:
#         uni = PyObject_GetAttrString(fn, "__code__")
#         rc = PyObject_HasAttrString(uni, "co_name")
#         if rc == 1:
#             uni = PyObject_Get
