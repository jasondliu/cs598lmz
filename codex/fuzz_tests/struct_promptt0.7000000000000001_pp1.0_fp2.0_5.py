import _struct
# Test _struct.Struct

def test_struct_simple():
    # Simple structs
    f1 = _struct.Struct('c')
    f2 = _struct.Struct('c'*6)
    f3 = _struct.Struct('6c')
    f4 = _struct.Struct('7c')
    f5 = _struct.Struct('cc')
    f6 = _struct.Struct('cccc')
    f7 = _struct.Struct('cccccccc')

    assert f1.size == 1
    assert f2.size == 6
    assert f3.size == 6
    assert f4.size == 7
    assert f5.size == 2
    assert f6.size == 4
    assert f7.size == 8

    assert f1.pack('A') == b'A'
    assert f2.pack('ABCDEF') == b'ABCDEF'
    assert f3.pack('ABCDEF') == b'ABCDEF'
    assert f4.pack('ABCDEFG') == b'ABCDEFG'
    assert f5.pack('AB') == b'AB'
   
