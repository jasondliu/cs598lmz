import _struct
# Test _struct.Struct

def test_type():
    S = _struct.Struct
    assert type(S('<b')) is S

def test_getter():
    S = _struct.Struct
    eq = equal
    eq(S('i')                   .format, 'i')
    eq(S('>H')                  .format, '>H')
    eq(S(b'>H')                 .format, '>H')
    eq(S(bytearray(b'>H'))      .format, '>H')
    eq(S(memoryview(bytearray(b'>H'))) .format, '>H')
    eq(S(memoryview(bytearray(b'>H')), 2) .format, '>HH')
    raises(TypeError, S, b'>H', 2)

def test_size():
    S = _struct.Struct
    eq = equal
    eq(S('i')                   .size, 4)
    eq(S('>H')                  .size, 2)
    eq(S(b'>H', 2)              .size
