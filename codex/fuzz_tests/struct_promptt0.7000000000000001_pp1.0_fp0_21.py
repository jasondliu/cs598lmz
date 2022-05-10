import _struct
# Test _struct.Struct("<i") on a struct of size 4
size = _struct.Struct("<i").size
assert size == 4
# Test _struct.Struct("<b") on a struct of size 1
size = _struct.Struct("<b").size
assert size == 1
# Test _struct.Struct("<c") on a struct of size 1
size = _struct.Struct("<c").size
assert size == 1
# Test _struct.Struct("<h") on a struct of size 2
size = _struct.Struct("<h").size
assert size == 2
# Test _struct.Struct("<l") on a struct of size 4
size = _struct.Struct("<l").size
assert size == 4
# Test _struct.Struct("<q") on a struct of size 8
size = _struct.Struct("<q").size
assert size == 8
# Test _struct.Struct("<B") on a struct of size 1
size = _struct.Struct("<B").size
assert size == 1
# Test _struct.Struct("<H") on a struct of size 2
size = _struct.Struct("
