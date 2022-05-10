import _struct
# Test _struct.Struct.__new__

def test_struct_new():
    with pytest.raises(TypeError):
        _struct.Struct()

    with pytest.raises(TypeError):
        _struct.Struct(1)

    with pytest.raises(TypeError):
        _struct.Struct(1, 2)

    with pytest.raises(TypeError):
        _struct.Struct('i', 2)

    with pytest.raises(TypeError):
        _struct.Struct('i', 2, 3)

    with pytest.raises(TypeError):
        _struct.Struct('i', 2, 3, 4)

    with pytest.raises(TypeError):
        _struct.Struct('i', 2, 3, 4, 5)

    with pytest.raises(TypeError):
        _struct.Struct('i', 2, 3, 4, 5, 6)

    with pytest.raises(TypeError):
        _struct.Struct('i', 2, 3, 4, 5, 6, 7)

    with pytest.raises(TypeError):
