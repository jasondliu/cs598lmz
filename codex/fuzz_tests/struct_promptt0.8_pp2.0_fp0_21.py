import _struct
# Test _struct.Struct
class S(Structure):
    _fields_ = [('i', c_int),
                ('f', c_float),
                ('s', c_char * 8),
                ]

format = "if20s"
format1 = "i8f40sf"
format2 = "<3i8f40sf"
format3 = "=3i8f40sf"

Struct = _struct.Struct
s = Struct(format)
# sz == 64
print s.size

print s.pack(1,2.0,"abcdefgh")
print s.pack_into(buffer(sbuffer), 0, 1,2.0,"abcdefgh")
print s.unpack(s.pack(1,2.0,"abcdefgh"))
print s.unpack_from(sbuffer, 0)

print s.unpack(s.pack(1,2.0,"abcdefgh") * 2) == s.unpack_from(sbuffer, 0) * 2

# must fail
try:
    s.unpack('hello')
except:
    print '
