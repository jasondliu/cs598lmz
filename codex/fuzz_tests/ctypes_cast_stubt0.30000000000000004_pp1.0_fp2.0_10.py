import ctypes
ctypes.cast(0, ctypes.py_object).value

# The ctypes module is a foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.

# The ctypes module provides a number of functions, mostly related to inspecting the C data types available, and instantiating and manipulating instances of those data types.

# The ctypes module provides a number of functions, mostly related to inspecting the C data types available, and instantiating and manipulating instances of those data types.

# ctypes.addressof(obj)
# Return the address of the raw memory buffer backing the object obj.

# ctypes.alignment(tp)
# Return the alignment requirements of the type tp.

# ctypes.byref(obj[, offset])
# Return a ctypes object pointing to the given object. The returned object is of type POINTER(type(obj)).

# ctypes.cast(obj, typ)
# Return a new instance of the given ctypes type initialized from the given object.

# ctypes.CFUNCTYPE
