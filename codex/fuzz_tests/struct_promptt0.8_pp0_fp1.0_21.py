import _struct
# Test _struct.Struct

# First test that we can make Struct objects with our new module
# and that they work as well as the ones from the normal struct module
s = _struct.Struct('bb')

test_values = [
    (1, 2),
    (-128, 127),
]

for value in test_values:
    s.pack(*value)
    assert s.unpack(s.pack(*value)) == value

s = _struct.Struct('')
s.pack()

s = _struct.Struct('>')
s.pack()

s = _struct.Struct('bb', 0)
s.pack()

# try some alignment tests
s = _struct.Struct('b<h')
assert s.pack(1, 2) == b'\x01\x00\x02'
assert s.unpack(b'\x01\x00\x02') == (1, 2)

s = _struct.Struct('b>h')
assert s.pack(1, 2) == b'\x01\x02\x00'
assert s.unpack
