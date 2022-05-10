import _struct
# Test _struct.Struct.format_size
assert _struct.Struct('<b').format_size() == 1
assert _struct.Struct('<b').format_size(1) == 1
assert _struct.Struct('<b').format_size('<b') == 1
assert _struct.Struct('<b').format_size('<b', 1) == 1
assert _struct.Struct('<b').format_size('<b', 1, 2) == 1
assert _struct.Struct('<b').format_size('<b', 1, 2, 3) == 1
assert _struct.Struct('<b').format_size('<b', 1, 2, 3, 4) == 1
assert _struct.Struct('<b').format_size('<b', 1, 2, 3, 4, 5) == 1
assert _struct.Struct('<b').format_size('<b', 1, 2, 3, 4, 5, 6) == 1
assert _struct.Struct('<b').format_size('<b', 1, 2, 3, 4, 5, 6, 7) == 1
assert _struct.Struct('<b').
