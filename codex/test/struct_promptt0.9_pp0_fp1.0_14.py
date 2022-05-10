import _struct
# Test _struct.Struct().format_size()
_struct.Struct("hh").format_size("@") == struct.calcsize("@hh")
# Test _struct.Struct().size
_struct.Struct("hh").size == struct.calcsize("hh")
# Test _struct.Struct().pack_into()
packedlen = _struct.Struct("hh").pack_into("", 0, 1, 2)
# Test _struct.Struct().unpack_from()
_struct.Struct("hh").unpack_from("", 0) == (1, 2)
# Test _struct.Struct().unpack()
_struct.Struct("hh").unpack("") == (1, 2)
# Test _struct.Struct().iter_unpack()
list(_struct.Struct("hh").iter_unpack("")) == [(1, 2)]
# Test _struct.Struct("hh").pack_into(), error handling with buffer too small
try:
    _struct.Struct("hh").pack_into("", -4, 1, 2);
except:
    pass  # OK
