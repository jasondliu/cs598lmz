import _struct
# Test _struct.Struct class
_struct.Struct(b'hhl')
_struct.Struct(b'hhl', b'<')
_struct.Struct(b'hhl', b'>')
_struct.Struct(b'hhl', b'@')
_struct.Struct(b'hhl', b'=')
_struct.Struct(b'hhl', b'!')
_struct.Struct(b'hhl', b'<')
_struct.Struct(b'hhl', b'@')
_struct.Struct(b'hhl', b'=')
_struct.Struct(b'hhl', b'!')
# Test _struct.Struct objects
struct1 = _struct.Struct(b'hhl')
struct2 = _struct.Struct(b'hhl', b'<')
struct3 = _struct.Struct(b'hhl', b'>')
struct4 = _struct.Struct(b'hhl', b'@')
struct5 = _struct.Struct(b'hhl', b'=')
struct6 = _struct.Struct(b'hhl', b'!
