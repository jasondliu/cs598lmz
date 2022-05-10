import ctypes
# Test ctypes.CField.
# See discussion at http://www.python.org/sf/1640394
class cS(ctypes.Structure):
    _fields_ = [
        ('value', ctypes.c_int),
        ('string', ctypes.c_char * 2)]
    _anonymous_ = ('string',)
s = cS(1, 'a', bytearray('b'))
print(s.value, s.string, s.string[0:2].tobytes(), sep='\n')

# Verify ctypes.CField handling is robust against TypeError coming out of
# _PyObject_GetDictPtr.
class DontGetDict(object):
    def __getattribute__(self, name):
        if '__dict__' == name:
            raise TypeError
        return super(DontGetDict, self).__getattribute__(name)

class T(DontGetDict, ctypes.Structure):
    _fields_ = []

# DontGetDict will cause ctypes to throw a TypeError when it tries to get
#
