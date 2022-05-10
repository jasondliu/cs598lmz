import ctypes
ctypes.cast(obj, ctypes.py_object).value

# The obj parameter must be a pointer to a PyObject.
# The value attribute of the ctypes.py_object instance is the original Python object.

# The following example shows how to wrap a Python object in a ctypes instance,
# and then retrieve the original object:

import ctypes
i = 42
c_intp = ctypes.cast(id(i), ctypes.POINTER(ctypes.c_int))
c_intp.contents.value

# The id() function returns the memory address of an object as an integer.
# The ctypes.cast() function casts the integer to a c_int pointer.
# The contents attribute of the pointer is the c_int instance.
# The value attribute of the c_int instance is the original integer value.

# The following example shows how to wrap a Python object in a ctypes instance,
# and then retrieve the original object:

import ctypes
i = 42
c_intp = ctypes.cast(id(i), ctypes.POINTER(ctypes.c_int))

