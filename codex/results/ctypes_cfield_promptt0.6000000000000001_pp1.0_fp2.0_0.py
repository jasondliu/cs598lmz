import ctypes
# Test ctypes.CField
class CTest(ctypes.Structure):
    _fields_ = [
        ('_x', ctypes.c_int),
        ('_y', ctypes.c_int),
        ]
    x = ctypes.CField('_x')

# Test ctypes.CField with a property
class PTest(ctypes.Structure):
    _fields_ = [
        ('_x', ctypes.c_int),
        ('_y', ctypes.c_int),
        ]
    x = ctypes.CField('_x')
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value

# Test ctypes.CField with a property and a getter
class GPTest(ctypes.Structure):
    _fields_ = [
        ('_x', ctypes.c_int),
        ('_y', ctypes.c_int),
        ]
    x = ctypes.CField('_x')
    @property
    def
