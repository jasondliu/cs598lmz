import _struct
# Test _struct.Struct.format
_struct.Struct.format.__doc__ = '''\
S.format -> string

Return a string containing the format string used to create this
Struct object.
'''

# Test _struct.Struct.size
_struct.Struct.size.__doc__ = '''\
S.size -> int

Return the size in bytes of a struct created from the format string
used to create this Struct object.
'''

# Test _struct.Struct.pack
_struct.Struct.pack.__doc__ = '''\
S.pack(v1, v2, ...) -> string

Return a string containing the values v1, v2, ... packed according to
the format string used to create this Struct object.
'''

# Test _struct.Struct.unpack
_struct.Struct.unpack.__doc__ = '''\
S.unpack(str) -> (v1, v2, ...)

Return a tuple containing values unpacked according to the format
string used to create this Struct object.
'''

# Test _struct.Struct.iter_unpack

