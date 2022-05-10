import _struct
# Test _struct.Struct with a format string of 'x'
# (this used to cause a segfault in older Pythons)
_struct.Struct('x')

# Test _struct.Struct with a format string of '!'
# (this used to cause a segfault in older Pythons)
_struct.Struct('!')

# Test _struct.Struct with a format string of 'c'
# (this used to cause a segfault in older Pythons)
_struct.Struct('c')

# Test _struct.Struct with a format string of 'cc'
# (this used to cause a segfault in older Pythons)
_struct.Struct('cc')

# Test _struct.Struct with a format string of 'cb'
# (this used to cause a segfault in older Pythons)
_struct.Struct('cb')

# Test _struct.Struct with a format string of 'b'
# (this used to cause a segfault in older Pythons)
_struct.Struct('b')

# Test _struct.Struct with a format string of 'bb'
# (
