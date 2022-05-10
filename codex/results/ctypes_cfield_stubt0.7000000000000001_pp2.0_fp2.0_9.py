import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

try:
    ctypes.c_buffer
except AttributeError:
    # ctypes.c_buffer doesn't exist before Python 2.6.
    pass
else:
    ctypes.CField = type(S.x)

# this shouldn't crash:
import _ctypes
ctypes.CField = type(S.x)

print 'Py_CField_Check() ==', _ctypes.Py_CField_Check(S.x)
print 'Py_CData_Check() ==', _ctypes.Py_CData_Check(S.x)
print 'Py_CField_Check() ==', _ctypes.Py_CField_Check(ctypes.c_int)
print 'Py_CData_Check() ==', _ctypes.Py_CData_Check(ctypes.c_int)
