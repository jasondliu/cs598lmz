import ctypes
# Test ctypes.CField.from_address()
X = ctypes.Structure('X')

malloc = ctypes._testcapi.malloc
free = ctypes._testcapi.free

class Y(ctypes.Structure):
    _fields_ = [('b', ctypes.c_byte)]

class Z(ctypes.Structure):
    _fields_ = [('a', Y)]

class U(ctypes.Union):
    _fields_ = [('a', Y),
                ('b', ctypes.c_uint8)]

class DynamicType(object):
    _fields_ = []
    def __init__(self):
        self._fields_.extend([
            ('a', Y),
            ('b', ctypes.c_ubyte),
            ('rest', Y*3),
        ])

    def alloc(self, n):
        class T(ctypes.Structure):
            _fields_ = self._fields_*n
        self.T = T
        pointer_type = ctypes.POINTER(self.T)
        self.p = pointer_
