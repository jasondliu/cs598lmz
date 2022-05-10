import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# check ctypes.CField
# check ctypes.CField.from_address
# check ctypes.CField.from_buffer
# check ctypes.CField.from_param
# check ctypes.CField.in_dll
# check ctypes.CField.in_dll_none
# check ctypes.CField.offset
# check ctypes.CField.size
# check ctypes.CField.value
