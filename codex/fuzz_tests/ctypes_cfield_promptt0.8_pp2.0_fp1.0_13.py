import ctypes
# Test ctypes.CField.from_address
field = ctypes.CField.from_address(ctypes.py_object(0),
                                   ctypes.py_object(0),
                                   ctypes.py_object(0),
                                   ctypes.py_object(0),
                                   (ctypes.py_object * 256)(),
                                   ctypes.py_object(0))

# Test ctypes.py_object
field.ob_type

# Test ctypes.PY_SSIZE_T_MAX
ctypes.PY_SSIZE_T_MAX

# Test ctypes.capi
ctypes.capi.PyType_Check(field)

# Test ctypes.CData.from_address
ctypes.CData.from_address(ctypes.py_object(0), ctypes.py_object(0))
