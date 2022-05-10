import _struct
# Test _struct.Struct
import sys

def test_struct_unpack(self):
    s = _struct.Struct('i')
    for format, arg, result in (('xcbhhiilfd',
                                (b'\x00\x01\x02', '\x03',
                                 b'\x04\x05', '\x06\x07\x08\t',
                                 '\x00\x01\x02\x03\x04\x05\x06\x07',
                                 '\x00\x01\x02\x03\x04\x05\x06\x07',
                                 10.0, 1.0),
                                (0x010203, 0x03, 0x0405, 0x06070809,
                                 0x00010203, 0x04050607, 0x00010203,
                                 0x04050607, 10.0, 1.0)),
                               ('7sxcbhhiilfd',
                                (b'\x00\x01\x02\x03\x04\
