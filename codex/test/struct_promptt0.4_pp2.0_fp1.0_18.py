import _struct
# Test _struct.Struct with all native formats
for code in _struct.__dict__:
    if code[0] == '_':
        continue
    if code in 'bhilfd':
        s = _struct.Struct(code)
        print(s.format)
        print(s.size)
        print(s.pack(0))
        print(s.pack(1))
        print(s.pack(2))
        print(s.pack(3))
        print(s.unpack(s.pack(0)))
        print(s.unpack(s.pack(1)))
        print(s.unpack(s.pack(2)))
        print(s.unpack(s.pack(3)))
        print(s.unpack(s.pack(0))[0] == 0)
        print(s.unpack(s.pack(1))[0] == 1)
        print(s.unpack(s.pack(2))[0] == 2)
        print(s.unpack(s.pack(3))[0] == 3)
# Test _struct.
