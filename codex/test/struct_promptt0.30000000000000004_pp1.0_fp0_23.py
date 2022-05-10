import _struct
# Test _struct.Struct

# Test __doc__
assert _struct.Struct.__doc__ == 'Compiled struct object'

# Test __new__
assert isinstance(_struct.Struct('i'), _struct.Struct)
assert isinstance(_struct.Struct('i', True), _struct.Struct)
assert isinstance(_struct.Struct('i', False), _struct.Struct)
assert isinstance(_struct.Struct('i', True, True), _struct.Struct)
assert isinstance(_struct.Struct('i', True, False), _struct.Struct)
assert isinstance(_struct.Struct('i', False, True), _struct.Struct)
assert isinstance(_struct.Struct('i', False, False), _struct.Struct)

# Test __init__
assert _struct.Struct('i').format == 'i'
assert _struct.Struct('i', True).format == '!i'
assert _struct.Struct('i', False).format == 'i'
assert _struct.Struct('i', True, True).format == '@i'
assert _struct.Struct('i', True, False).format == '!i'
