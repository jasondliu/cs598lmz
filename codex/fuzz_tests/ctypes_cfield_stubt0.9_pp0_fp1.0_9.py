import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert isinstance(S.x, ctypes.CField)
assert issubclass(ctypes.CField, types.MemberDescriptorType)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

ctypes.CData = type(S().x)
assert isinstance(S().x, ctypes.CData)
assert issubclass(ctypes.CData, ctypes.c_char_p)
assert ctypes.CData == ctypes.c_char_p

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.py_object)]

ctypes._Pointer = type(S.x)
assert isinstance(S.x, ctypes._Pointer)
assert issubclass(ctypes._Pointer, types.MemberDescriptorType)

assert ctypes.POINTER == ctypes.POINTER(ctypes.c_int)
assert ctypes.POINTER(ctypes.c_int) == ctypes.POINTER(ctypes.
