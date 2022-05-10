import _struct
# Test _struct.Struct
struct_test_cases = [
    ('i', 2**31 - 1, b'\xff\xff\xff\x7f'),
    ('i', -2**31, b'\x00\x00\x00\x80'),
    ('i', 0, b'\x00\x00\x00\x00'),
    ('i', 2**31, b'\x00\x00\x00\x80'),
    ('i', -2**31 - 1, b'\xff\xff\xff\x7f'),
    ('i', 2**15 - 1, b'\xff\x7f'),
    ('i', -2**15, b'\x00\x80'),
    ('i', 0, b'\x00\x00'),
    ('i', 2**15, b'\x00\x80'),
    ('i', -2**15 - 1, b'\xff\x7f'),
    ('i', 2**7 - 1, b'\x7f'),
    ('i', -2**7, b'\x80'),
