import _struct
# Test _struct.Struct

# Test __new__
assert _struct.Struct('hhl').format == b'<hhl'
assert _struct.Struct('>hhl').format == b'>hhl'
assert _struct.Struct('@hhl').format == b'@hhl'
assert _struct.Struct('=hhl').format == b'=hhl'

# Test __repr__
assert repr(_struct.Struct('hhl')) == "Struct('<hhl')"
assert repr(_struct.Struct('@hhl')) == "Struct('@hhl')"

# Test __len__
assert len(_struct.Struct('hhl')) == _struct.calcsize('hhl')

# Test __getitem__
assert _struct.Struct('hhl')[0] == 'h'
assert _struct.Struct('hhl')[1] == 'h'
assert _struct.Struct('hhl')[2] == 'l'
assert _struct.Struct('hhl')[3] == 'x'

# Test pack/unpack/unpack_from
