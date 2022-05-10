import ctypes
# Test ctypes.CField
try:
    ctypes.CField
except AttributeError:
    raise ImportError("this version of ctypes has no CField")

# Test ctypes.CField.from_address
try:
    ctypes.CField.from_address
except AttributeError:
    raise ImportError("this version of ctypes has no CField.from_address")

# Test ctypes.CField.from_buffer
try:
    ctypes.CField.from_buffer
except AttributeError:
    raise ImportError("this version of ctypes has no CField.from_buffer")

# Test ctypes.CField.from_param
try:
    ctypes.CField.from_param
except AttributeError:
    raise ImportError("this version of ctypes has no CField.from_param")

# Test ctypes.CField.in_dll
try:
    ctypes.CField.in_dll
except AttributeError:
    raise ImportError("this version of ctypes has no CField.in_dll")

# Test ctypes.CField.in_
