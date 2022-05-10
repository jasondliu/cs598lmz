import ctypes
# Test ctypes.CField.from_param
ctypes.CField.from_param(ctypes.c_char_p(), 10)

# Test ctypes.CField.from_param with unexpected type
ctypes.CField.from_param(ctypes.c_char_p(), "10")

# Test ctypes.CField.from_address
ctypes.string_at(ctypes.CField.from_address(ctypes.addressof(ctypes.c_char_p()), ctypes.sizeof(ctypes.c_char_p())).value, 5)

# Test ctypes.CField.from_buffer
ctypes.string_at(ctypes.CField.from_buffer(ctypes.c_char_p(), 0, ctypes.sizeof(ctypes.c_char_p())).value, 5)

# Test convenience method py_object.from_param
ctypes.py_object.from_param(42)

# Test convenience method py_object.from_address
ctypes.py_object.from_address(ctypes.addressof(ctypes
