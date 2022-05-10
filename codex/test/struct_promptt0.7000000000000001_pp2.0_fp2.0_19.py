import _struct
# Test _struct.Struct.format
assert _struct.Struct('x').format == 'x'
assert _struct.Struct('x:1').format == 'x:1'
assert _struct.Struct('x:1x:1').format == 'x:1x:1'
assert _struct.Struct('x:2P').format == 'x:2P'
assert _struct.Struct('x:1P').format == 'x:1P'
assert _struct.Struct('x:3P').format == 'x:3P'
assert _struct.Struct('x:2P').format == 'x:2P'
assert _struct.Struct('x:2P').format == 'x:2P'
assert _struct.Struct('x:2P').format == 'x:2P'
assert _struct.Struct('x:2P').format == 'x:2P'
assert _struct.Struct('x:2P').format == 'x:2P'
assert _struct.Struct('x:2P').format == 'x:2P'
assert _struct.Struct('P').format == 'P'
assert _struct
