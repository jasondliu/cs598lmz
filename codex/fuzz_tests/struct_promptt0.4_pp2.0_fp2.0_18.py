import _struct
# Test _struct.Struct

def test_struct_error():
    with pytest.raises(TypeError):
        _struct.Struct()

def test_struct_format():
    with pytest.raises(TypeError):
        _struct.Struct('')

def test_struct_size():
    with pytest.raises(TypeError):
        _struct.Struct('', '')

def test_struct_format_size():
    with pytest.raises(TypeError):
        _struct.Struct('', 0, '')

def test_struct_format_size_error():
    with pytest.raises(TypeError):
        _struct.Struct('', 0, '', '')

def test_struct_format_size_error_ok():
    _struct.Struct('', 0, '', True)

def test_struct_pack():
    with pytest.raises(TypeError):
        _struct.Struct('', 0).pack()

def test_struct_pack_error():
    with pytest.raises(TypeError):
        _struct.Struct('',
