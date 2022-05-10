import ctypes
# Test ctypes.CField, .offset, .size, .type and .name
#
# These should suggest that the compiler can do the same
# without all the complicated code in the class.
class C(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_short),
        ("b", ctypes.c_char),
        ("c", ctypes.c_int),
        ("d", ctypes.c_byte),
        ("e", ctypes.c_long),
        ("f", ctypes.c_char),
    ]

    def __repr__(self):
        return "C(a=%d, b=%r, c=%d, d=%d, e=%d, f=%r)" % (
            self.a, self.b, self.c, self.d, self.e, self.f)

    def __str__(self):
        return repr(self)

for name in "abcde":
    field = getattr(C, name)
    print name, field.offset, field.type, field.size

