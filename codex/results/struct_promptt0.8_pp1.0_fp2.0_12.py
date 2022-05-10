import _struct
# Test _struct.Struct.unpack_from
packer = _struct.Struct('IIP')
size = packer.size
data = packer.pack(1, 2, 3)
offset = 0
assert packer.unpack_from(data, offset) == (1, 2, 3)
offset += size
assert packer.unpack_from(data, offset) == (1, 2, 3)

# Test _struct.Struct.iter_unpack
packer = _struct.Struct('IIP')
size = packer.size
data = packer.pack(1, 2, 3)
it = packer.iter_unpack(data)
assert next(it) == (1, 2, 3)
assert next(it) == (1, 2, 3)

packer = _struct.Struct('IIP')
size = packer.size
data = packer.pack(1, 2, 3)
it = packer.iter_unpack(data)
assert next(it) == (1, 2, 3)
try:
    next(it)
except StopIteration:
    pass
