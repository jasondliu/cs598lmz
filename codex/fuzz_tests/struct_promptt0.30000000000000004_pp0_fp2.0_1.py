import _struct
# Test _struct.Struct.format_size
assert _struct.Struct('i').format_size('<') == 4
assert _struct.Struct('i').format_size('>') == 4
assert _struct.Struct('i').format_size('!') == 4
assert _struct.Struct('i').format_size('=') == 4
assert _struct.Struct('i').format_size('<') == 4
assert _struct.Struct('i').format_size('>') == 4
assert _struct.Struct('i').format_size('!') == 4
assert _struct.Struct('i').format_size('=') == 4
assert _struct.Struct('i').format_size('<') == 4
assert _struct.Struct('i').format_size('>') == 4
assert _struct.Struct('i').format_size('!') == 4
assert _struct.Struct('i').format_size('=') == 4
assert _struct.Struct('i').format_size('<') == 4
assert _struct.Struct('i').format_size('>') == 4
assert _struct.Struct('i').format_size('!
