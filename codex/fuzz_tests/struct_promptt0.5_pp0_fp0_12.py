import _struct
# Test _struct.Struct

def test_Struct():
    # test the constructor
    assert _struct.Struct('i')
    assert _struct.Struct('ii')
    assert _struct.Struct('hh')
    assert _struct.Struct('hhh')
    assert _struct.Struct('hhhh')
    assert _struct.Struct('b')
    assert _struct.Struct('bb')
    assert _struct.Struct('bbb')
    assert _struct.Struct('bbbb')
    assert _struct.Struct('B')
    assert _struct.Struct('BB')
    assert _struct.Struct('BBB')
    assert _struct.Struct('BBBB')
    assert _struct.Struct('h')
    assert _struct.Struct('hh')
    assert _struct.Struct('hhh')
    assert _struct.Struct('hhhh')
    assert _struct.Struct('H')
    assert _struct.Struct('HH')
    assert _struct.Struct('HHH')
    assert _struct.Struct('HHHH')
    assert _struct.Struct('l')
    assert _struct.Struct('ll')
    assert _struct.Struct('
