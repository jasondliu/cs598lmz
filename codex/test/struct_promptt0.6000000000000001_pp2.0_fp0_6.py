import _struct
# Test _struct.Struct

# Verify that the constructors accept all kinds of strings
for t in _struct.__dict__.keys():
    if t[0] == '_' or not t.isupper():
        continue
    s = _struct.Struct(t)
    s = _struct.Struct(t + '>')
    s = _struct.Struct(t + '<')
    s = _struct.Struct(t + '!')

# Verify that the format strings are stored correctly
for t in _struct.__dict__.keys():
    if t[0] == '_' or not t.isupper():
        continue
    for endianness in ('>', '<', '!'):
        s = _struct.Struct(t + endianness)
        assert s.format == t + endianness

# Verify that the size is computed correctly
for t in _struct.__dict__.keys():
    if t[0] == '_' or not t.isupper():
        continue
    for endianness in ('>', '<', '!'):
        s = _struct.Struct
