import _struct
# Test _struct.Struct.format_size
assert _struct.Struct('@I').format_size('@I') == 4
assert _struct.Struct('@I').format_size('<I') == 4
assert _struct.Struct('@I').format_size('<I', '@I') == 4
assert _struct.Struct('@I').format_size('<I', '<I') == 4
assert _struct.Struct('@I').format_size('@I', '@I') == 4
assert _struct.Struct('@I').format_size('@I', '<I') == 4
assert _struct.Struct('@I').format_size('<I', '@I', '<I') == 8
assert _struct.Struct('@I').format_size('<I', '@I', '@I') == 8
assert _struct.Struct('@I').format_size('<I', '@I', '<I', '@I') == 12
assert _struct.Struct('@I').format_size('<I', '@I', '<I', '@I', '<I') == 16
