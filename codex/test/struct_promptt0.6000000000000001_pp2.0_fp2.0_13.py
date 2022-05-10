import _struct
# Test _struct.Struct objects
def test_struct_objects():
    s = _struct.Struct('i')
    assert s.size == _struct.calcsize('i')
    assert s.format == 'i'
    s = _struct.Struct('ii')
    assert s.size == _struct.calcsize('ii')
    assert s.format == 'ii'
    s = _struct.Struct('3i')
    assert s.size == _struct.calcsize('3i')
    assert s.format == '3i'
    s = _struct.Struct('i3i')
    assert s.size == _struct.calcsize('i3i')
    assert s.format == 'i3i'
    s = _struct.Struct('i6i')
    assert s.size == _struct.calcsize('i6i')
    assert s.format == 'i6i'
    s = _struct.Struct('i' * 1000)
    assert s.size == _struct.calcsize('i' * 1000)
    assert s.format == 'i' * 1000
   
