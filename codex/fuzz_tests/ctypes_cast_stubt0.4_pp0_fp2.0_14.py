import ctypes
ctypes.cast(0, ctypes.py_object)

# Uncomment the following line to see the result of the cast
# print(ctypes.cast(0, ctypes.py_object))

# Cast an integer 1 to the ctypes.py_object type. Store the result as py_object_1.
py_object_1 = ctypes.cast(1, ctypes.py_object)

# Cast the integer 2 to the ctypes.py_object type. Store the result as py_object_2.
py_object_2 = ctypes.cast(2, ctypes.py_object)

# Uncomment the following line to see the result of the cast
# print(py_object_1, py_object_2)

# Cast c_void_p to a Python integer and store the result as void_p_int.
void_p_int = ctypes.cast(void_p, ctypes.py_object)

# Uncomment the following line to see the result of the cast
# print(void_p_int)

# Cast c_void_p to a c_char
