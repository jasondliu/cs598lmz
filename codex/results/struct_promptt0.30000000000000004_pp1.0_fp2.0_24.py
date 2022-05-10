import _struct
# Test _struct.Struct.format_size
assert _struct.Struct('i').format_size('<') == _struct.calcsize('<i')
assert _struct.Struct('i').format_size('>') == _struct.calcsize('>i')
assert _struct.Struct('i').format_size('!') == _struct.calcsize('!i')

# Test _struct.Struct.size
assert _struct.Struct('i').size == _struct.calcsize('i')
assert _struct.Struct('i').size == _struct.calcsize('>i')
assert _struct.Struct('i').size == _struct.calcsize('!i')

# Test _struct.Struct.format
assert _struct.Struct('i').format == 'i'
assert _struct.Struct('i').format == '>i'
assert _struct.Struct('i').format == '!i'

# Test _struct.Struct.pack
assert _struct.Struct('i').pack(1) == _struct.pack('i', 1)
assert _struct.Struct('i').pack(1) == _
