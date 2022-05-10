import _struct
# Test _struct.Struct

with _struct.Struct('i') as s:
    print(s)
    print(s.size)
    print(s.pack(1))
    print(s.unpack(s.pack(1)))
    print(s.unpack_from(s.pack(1), 0))

with _struct.Struct('ii') as s:
    print(s)
    print(s.size)
    print(s.pack(1, 2))
    print(s.unpack(s.pack(1, 2)))
    print(s.unpack_from(s.pack(1, 2), 0))

with _struct.Struct('iii') as s:
    print(s)
    print(s.size)
    print(s.pack(1, 2, 3))
    print(s.unpack(s.pack(1, 2, 3)))
    print(s.unpack_from(s.pack(1, 2, 3), 0))

with _struct.Struct('iiii') as s:
    print(s)
    print(s
