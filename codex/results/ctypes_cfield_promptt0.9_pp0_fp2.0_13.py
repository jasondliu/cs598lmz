import ctypes
# Test ctypes.CField() format specifier

S1 = struct.Struct('bhil')
CField = ctypes.CField

f1 = CField(S1, 0, 'c', S1._length_ * S1._length_)
f2 = CField(S1, 0, 'c', S1._length_ / 2)
f3 = CField(S1, 0, 'c', 100)

f1(b'\x00', S1.size)
f2(b'\x00', S1.size)
f3(b'\x00', S1.size)
