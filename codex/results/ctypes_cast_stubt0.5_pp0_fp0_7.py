import ctypes
ctypes.cast(1, ctypes.py_object)
# <__main__.PyObject_HEAD object at 0x7f2b1c7b2d00>

ctypes.cast(1, ctypes.py_object).value
# 1

# py_object is a struct with a single member, ob_ref.
# On 32-bit builds, ob_ref is a pointer to the object.
# On 64-bit builds, ob_ref is the object itself.

# The PyObject_HEAD macro is defined in Include/object.h:
#
# #define PyObject_HEAD                   \
#         PyObject ob_base;               \
#         Py_ssize_t ob_size; /* Number of items in variable part */
#
# So the struct is a PyObject, which is the C representation of a Python
# object, and a Py_ssize_t, which is an integer.
#
# The PyObject struct is defined in Include/cpython/object.h:
#
# typedef struct _object {
#         _PyObject_HEAD_EXTRA
#         Py_ss
