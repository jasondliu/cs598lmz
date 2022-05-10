import _struct
# Test _struct.Struct

s = _struct.Struct('i')
s.size
s.pack(1)
s.unpack(s.pack(1))
s.unpack(s.pack(1))[0]
s.pack_into(b'12345678', 4, 2)
s.unpack_from(b'12345678', 4)
s.unpack_from(b'12345678', 4)[0]

# Issue #6115: test the alignment of the struct format
_struct.Struct('cx').size
_struct.Struct('xc').size
_struct.Struct('sx').size
_struct.Struct('xs').size
_struct.Struct('ix').size
_struct.Struct('xi').size

# Issue #6115: test the alignment of the struct format
# with the new alignment feature
_struct.Struct('@cx').size
_struct.Struct('@xc').size
_struct.Struct('@sx').size
_struct.Struct('@xs').size
_struct.Struct('@ix').size
_struct.Struct('@xi').size
