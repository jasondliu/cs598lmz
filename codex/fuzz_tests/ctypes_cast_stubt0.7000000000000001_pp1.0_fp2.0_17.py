import ctypes
ctypes.cast(ptr, ctypes.py_object).value

# C:
# PyObject* ptr = ...;
# PyObject* item = PyArray_GETPTR2(ptr, y, x);
# double value = *((double*) PyArray_DATA(item));

# C++
ptr.get_ptr(y, x).get_data()

# C++
# ptr.get_ptr(y, x).get_dtype()
# ptr.get_ptr(y, x).get_shape()
# ptr.get_ptr(y, x).get_strides()

ptr = ptr.get_ptr(y, x)
ptr2 = ptr.get_ptr(y2, x2)

# C:
# PyObject* ptr = ...;
# PyObject* item = PyArray_GETPTR3(ptr, z, y, x);
# double value = *((double*) PyArray_DATA(item));

# C++
ptr.get_ptr(z, y, x).get_data()

# C:
# PyObject* ptr = ...;
