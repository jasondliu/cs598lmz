import _struct
# Test _struct.Struct

struct_tests = [
    ('h', 2),
    ('i', 4),
    ('l', 4),
    ('q', 8),
    ('H', 2),
    ('I', 4),
    ('L', 4),
    ('Q', 8),
    ('f', 4),
    ('d', 8),
    ('P', _struct.calcsize('P')),
    ('s', 1),
    ('p', 1),
]

for fmt, size in struct_tests:
    s = _struct.Struct(fmt)
    print(fmt, s.size, size)
    assert s.size == size
    print(s.pack(1))
    print(s.unpack(s.pack(1)))

# Test _struct.Struct.iter_unpack

s = _struct.Struct('hhh')
data = s.pack(1, 2, 3)
print(list(s.iter_unpack(data)))

# Test _struct.Struct.iter_unpack with offset

s = _struct.Struct('hhh')
data
