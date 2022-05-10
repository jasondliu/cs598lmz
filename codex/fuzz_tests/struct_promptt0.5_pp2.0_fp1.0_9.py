import _struct
# Test _struct.Struct
with open('test/data/struct_test.bin', 'rb') as f:
    data = f.read()

s = _struct.Struct('BHl')
values = s.unpack(data)

assert values == (10, 255, 987654321)

# Test _struct.Struct.iter_unpack
with open('test/data/struct_test.bin', 'rb') as f:
    data = f.read()

s = _struct.Struct('BHl')
values = list(s.iter_unpack(data))

assert values == [(10, 255, 987654321)]

# Test _struct.Struct.pack_into
with open('test/data/struct_test.bin', 'rb') as f:
    data = f.read()

buf = bytearray(len(data))

s = _struct.Struct('BHl')
s.pack_into(buf, 0, 10, 255, 987654321)

assert buf == data

# Test _struct.Struct.iter_un
