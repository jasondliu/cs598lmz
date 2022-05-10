import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    y = ctypes.c_uint8
    z = ctypes.c_uint8

    def __repr__(self):
        return '{0}.{1}.{2}'.format(self.x, self.y, self.z)

s = S()
s.x = 1
s.y = 2
s.z = 3
print(s)

a = ctypes.c_uint8 * 3
b = a(1, 2, 3)
print(b)
