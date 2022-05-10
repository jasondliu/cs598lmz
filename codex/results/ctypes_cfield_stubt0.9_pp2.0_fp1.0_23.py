import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# issue31_test
class CFuncPtr(ctypes.CFuncPtr):
    _fields_ = [("name", ctypes.c_char_p)]

def funcptr_special(value):
    if isinstance(value, CFuncPtr):
        return value.name, repr(value.value)
    return value

Support.print_dict.specialfuncs["funcptr"] = funcptr_special

f = CFuncPtr(None)
print(f)
f = CFuncPtr(ctypes.Structure._fields_)
print(f)
print_dict(vars(ctypes))

# issue 32: __array_struct__ accessor
import numpy
numpy.arange(11, dtype=float).tolist()
np_arr = numpy.arange(11, dtype=float)
np_arr.tolist()

# issue 33: unicode
if sys.version_info[0] < 3:
    text = unicode('abcd', 'ascii')
else:
    text = bytes('abcd',
