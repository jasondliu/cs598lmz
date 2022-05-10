import _struct
# Test _struct.Struct.__repr__
_struct.Struct("hBcb").__repr__()
_struct.Struct("hBcb").__repr__(1)

# Test _struct.Struct.unpack_from
_struct.Struct("hBcb").unpack_from()
_struct.Struct("hBcb").unpack_from(1)

# Test _struct.Struct.iter_unpack
_struct.Struct("hBcb").iter_unpack()
_struct.Struct("hBcb").iter_unpack(1)

# Test _struct.Struct.pack
_struct.Struct("hBcb").pack()
_struct.Struct("hBcb").pack(1)

# Test _struct.Struct.pack_into
_struct.Struct("hBcb").pack_into()
_struct.Struct("hBcb").pack_into(1)

# Test _struct.Struct.size
_struct.Struct("hBcb").size
_struct.Struct("hBcb").size()
_struct.Struct("hBcb").size(1)
