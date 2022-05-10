import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a hack to get around the fact that the Python C API doesn't
# provide a way to get the value of a PyObject* when it's known that
# the PyObject* is a PyLongObject*.
#
# The Python C API docs are here:
# https://docs.python.org/3/c-api/long.html
#
# The PyLongObject struct is defined in longintrepr.h:
# https://github.com/python/cpython/blob/master/Include/longintrepr.h
#
# The PyLongObject struct looks like this:
#
# typedef struct _longobject PyLongObject;
# struct _longobject {
#     PyObject_VAR_HEAD
#     digit ob_digit[1];
# };
#
# The PyObject_VAR_HEAD struct looks like this:
#
# #define PyObject_VAR_HEAD \
#     PyObject_HEAD \
#     Py_ssize_t ob_size; /* Number of items in variable part */

