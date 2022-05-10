import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_fields(d):
    S._fields_ = [('x', ctypes.c_int)]
    S._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    S._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int)]
    S._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int), ('w', ctypes.c_int)]

def test_fields_mapping(d):
    S._fields_ = [('x', ctypes.c_int)]
    S._fields_ = {'x': ctypes.c_int}
    S._fields_ = OrderedDict([('x', ctypes.c_int)])
    S._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    S._fields_ = {'x': ctypes.c
