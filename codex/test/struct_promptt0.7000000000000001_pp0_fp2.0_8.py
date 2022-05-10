import _struct
# Test _struct.Struct
print(_struct.Struct('2h 3h').size)
print(_struct.Struct('2h 3h').pack(1, 2, 3, 4, 5))
print(_struct.Struct('2h 3h').unpack('\1\0\2\0\3\0\4\0\5\0'))

# Test _struct.pack
print(_struct.pack('>i', 5))
print(_struct.pack('>i', -5))
print(_struct.pack('>h', 5))
print(_struct.pack('>h', -5))
print(_struct.pack('>b', 5))
print(_struct.pack('>b', -5))
print(_struct.pack('>hhb', 5, 6, -5))
print(_struct.pack('>i', 0x12345678))
print(_struct.pack('>d', 0.42))
print(_struct.pack('>i', 0x7fffffff))
print(_struct.pack('>i', 0x80000000))

# Test _struct.unpack
