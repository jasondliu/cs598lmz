import _struct
# Test _struct.Struct.__new__
class TestNew(_struct.Struct):
    _format = 'ii'
    _size = _struct.calcsize(_format)
class TestNewValueError(_struct.Struct):
    _format = 'i'
    _size = _struct.calcsize(_format)
class TestNewOverflowError(_struct.Struct):
    _format = 'I'
    _size = _struct.calcsize(_format)
# Test _struct.unpack
class TestUnpack(_struct.Struct):
    _format = 'ii'
    _size = _struct.calcsize(_format)
# Test _struct.Struct._substruct
# XXX: Doesn't work yet.
class TestSubStruct(_struct.Struct):
    _format = 'ii'
    _size = _struct.calcsize(_format)
class TestSubStructArray(_struct.Struct):
    _format = 'ii'
    _size = _struct.calcsize(_format)
class TestSubStructSubStruct(_struct.Struct):
    _format = 'ii'
    _size = _struct.calcs
