import _struct
# Test _struct.Struct.__format__ with 's' and 'r'.
# Issue #28210: _struct.Struct.__format__('s') should return the format string.
# Issue #28211: _struct.Struct.__format__('r') should return the repr of the
#               format string.
# Issue #28212: _struct.Struct.__format__('') should raise ValueError.
# Issue #28213: _struct.Struct.__format__('S') should raise ValueError.
fmt = '<4shl'
s = _struct.Struct(fmt)
msg = '_struct.Struct.__format__("{}") should be "{}"'
expected = '<4shl'
assert s.__format__('s') == expected, msg.format('s', expected)
expected = "<Struct object at 0x{:x}>".format(id(s))
assert s.__format__('r') == expected, msg.format('r', expected)
with pytest.raises(ValueError, match='__format__: empty format string'):
    s.__format__(
