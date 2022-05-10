import _struct
# Test _struct.Struct

# Test for issue #12768
_struct.Struct('<x123s').size
_struct.Struct('009>').size
_struct.Struct('@324').size
_struct.Struct('@*').size
_struct.Struct('@*0').size
_struct.Struct('@*1').size
_struct.Struct('@*0s').size
_struct.Struct('@*1s').size
_struct.Struct('@*2s').size

# Test for issue #26555
_struct.Struct(b'<2i').size
_struct.Struct(b'<x2i').size
_struct.Struct(b'<2i x').size
_struct.Struct(b'<2i x').size
_struct.Struct(b'<2i x 2i').size
