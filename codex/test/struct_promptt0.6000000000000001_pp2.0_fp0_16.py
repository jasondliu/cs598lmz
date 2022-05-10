import _struct
# Test _struct.Struct

def test_struct():
    import _struct
    assert _struct.Struct('i').size == 4
    assert _struct.Struct('ii').size == 8
    raises(TypeError, _struct.Struct, 'i', 'i')
    raises(TypeError, _struct.Struct, 'ii', 'i')
    raises(TypeError, _struct.Struct, 'ii', alignment=2)
    assert _struct.Struct('i', native=1).size == 4
    assert _struct.Struct('ii', native=1).size == 8
    assert _struct.Struct('i', native=1, alignment=1).size == 4
    assert _struct.Struct('ii', native=1, alignment=1).size == 8
    assert _struct.Struct('i', native=0, alignment=1).size == 4
    assert _struct.Struct('ii', native=0, alignment=1).size == 8
    assert _struct.Struct('i', native=0, alignment=2).size == 4
    assert _struct.Struct('ii', native=0, alignment=2).size == 8
