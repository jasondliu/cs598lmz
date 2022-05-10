import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.Field = type(S._fields_[0])

PField = ctypes.POINTER(ctypes.CField)

class Meta(ctypes.CFuncPtr):
    _fields_ = [('__name__', ctypes.c_char_p),
                ('__module__', ctypes.c_char_p),
                ('__dict__', ctypes.py_object),
                ('__doc__', ctypes.c_char_p),
                ('__text_signature__', ctypes.c_char_p),
                ('__annotations__', ctypes.py_object),
                ('__orig_bases__', ctypes.py_object)]

class Dict(ctypes.PyDictObject):
    _fields_ = [('length', ctypes.c_ssize_t),
                ('version_tag', ctypes.c_long),
                ('ma_keys', ctypes.py_object),
                ('ma_values', ctypes.py_object),
                ('ma_used', ctypes.c_ssize_t),
