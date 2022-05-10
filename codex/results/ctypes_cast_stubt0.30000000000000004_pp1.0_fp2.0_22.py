import ctypes
ctypes.cast(0, ctypes.py_object).value

# The address of the object is the same as the address of the value.
ctypes.cast(id(0), ctypes.py_object).value is 0

# ctypes can also create new objects by calling the constructor.
ctypes.py_object(id)

# The address of the constructed object is different.
ctypes.cast(id(id), ctypes.py_object).value is id

# ctypes can also access the ob_refcnt and ob_type attributes of objects.
ctypes.cast(id(0), ctypes.py_object).ob_refcnt
ctypes.cast(id(0), ctypes.py_object).ob_type

# The type is also an object, and its reference count is greater than one.
ctypes.cast(id(int), ctypes.py_object).ob_refcnt

# The type of a type is 'type'.
ctypes.cast(id(int), ctypes.py_object).ob_type is type

# The reference count of 'type' is
