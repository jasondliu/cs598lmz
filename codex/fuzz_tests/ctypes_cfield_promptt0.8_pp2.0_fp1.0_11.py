import ctypes
# Test ctypes.CField
import _testcapi
class POINT(ctypes.Structure):
    _fields_ = (('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_float),
                ('zz', ctypes.c_float),
                )

class POINT_FIELD(ctypes.Structure):
    _fields_ = (ctypes.CField('x'),
                'y',
                ('z', ctypes.c_float))

class POINT_FIELD2(ctypes.Structure):
    _fields_ = (ctypes.CField('x'),
                ctypes.CField('y'),
                ('z', ctypes.c_float))

class POINT_FIELD_TEST(ctypes.Structure):
    _fields_ = (('x', ctypes.c_int),
                ctypes.CField('y'),
                ('z', ctypes.c_float))

class POINT_TYPE(ctypes.Structure):
    _fields_ = (('x', ctypes.c_
