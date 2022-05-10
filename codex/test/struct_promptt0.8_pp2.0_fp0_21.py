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
