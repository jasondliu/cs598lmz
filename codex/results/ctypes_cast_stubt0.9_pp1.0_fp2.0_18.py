import ctypes
ctypes.cast(pointer, ctypes.py_object).value

# or
ctypes.addressof(pointer.contents)

# to convert pointer to array
# cast to py_obect and then do
# new_pointer = type(pointer) # e.g. c_int * 2
# new_pointer.from_address(id(new_pointer))
</code>

