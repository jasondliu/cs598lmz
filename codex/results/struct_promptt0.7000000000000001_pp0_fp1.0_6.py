import _struct
# Test _struct.Struct
from test import support

# This tests the internal _struct module; it doesn't test the struct module
# as you'd use it to pack and unpack data.

def test_struct_unpack():
    for fmt, expected, data in [
       ('i', [1234], b'\xd2\x04\x00\x00'),
       ('!i', [1234], b'\x00\x00\x04\xd2'),
       ('xcbx', [b'', b'a', b''], b'a\x00'),
       ('ihh', [1, 2, 3], b'\x01\x00\x00\x00\x02\x00\x03\x00'),
       ('IHh', [1, 2, 3], b'\x01\x00\x00\x00\x02\x00\x03\x00'),
       ('IHh', [1, 2, 3], b'\x01\x00\x00\x00\x02\x00\x03\x00\x00'),
