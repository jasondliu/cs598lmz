import ctypes

class S(ctypes.Structure):
    x = 0
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]
    _x_has_value = False

    @property
    def y(self):
        return self._y + self.x

    @y.setter
    def y(self, value):
        self._y = value

s = S()
s.x = 3
s.y = 5
ctypes.pointer(s).contents
print('after:\n', s.x, s.y)
