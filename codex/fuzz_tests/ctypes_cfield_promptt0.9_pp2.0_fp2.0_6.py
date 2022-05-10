import ctypes
# Test ctypes.CField() and ctypes.Field()
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_char),
                ("d", ctypes.c_char),
                ('e', ctypes.c_short),
                ('f', ctypes.c_short),
                ('g', ctypes.c_int)]
    def v(self):
        return self.a + self.d + self.e + self.f + self.g

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_char),
                ("d", ctypes.c_char),
                ('e', ctypes.c_short),
                ('f', ctypes.c_short),
                ('g', ctypes.c_int)]

#print int(ctypes.addressof(X.a))
print X.
