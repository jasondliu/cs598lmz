from _struct import Struct
s = Struct.__new__(Struct)
s.format = b'<4s4s'
s.size = s.calcsize(s.format)

print(s.size)
print(s.pack(b'test', b'1234'))
print(s.unpack_from(b'test1234', 1))

# 类方法第一个参数是cls
class S(Struct):
    _fields_ = [('a', '<h'), ('b', '<i')]

print(S.size)
print(S.pack(1, 2))
print(S.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00', 0))

def unpack_from(fmt, data, offset=0):
    s = Struct.__new__(Struct)
    s.format = fmt
    s.size = s.calcsize(fmt)
    return s.unpack_from(data, offset)

print(unpack_from('>HH
