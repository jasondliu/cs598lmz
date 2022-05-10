import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulong(1)
    _fields_ = [('x', ctypes.c_ulong)]

    @classmethod
    def _pack_(cls, value):
        return ctypes.c_ulong(value)

    @classmethod
    def _unpack_(cls, value):
        return int(value)

    def _get_(self):
        return self.x.value

    def _set_(self, value):
        self.x = ctypes.c_ulong(value)

s = S()
s.x = 5
print(s.x)
s.x = 0x10
print(s.x)

print(s._pack_(0x10))
print(s._unpack_(0x10))

s._set_(0x10)
print(s._get_())

s = S()
print(s.x)
s = S(0x10)
print(s.x)
s = S(x=0x10)
print(s.x)
s = S(x=0x
