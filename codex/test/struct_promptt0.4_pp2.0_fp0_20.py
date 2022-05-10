import _struct
# Test _struct.Struct

def test_struct_error():
    # Issue #14077: _struct.Struct() should raise ValueError for bad format.
    with pytest.raises(ValueError):
        _struct.Struct("")
    with pytest.raises(ValueError):
        _struct.Struct("<")
    with pytest.raises(ValueError):
        _struct.Struct("<b")
    with pytest.raises(ValueError):
        _struct.Struct("<b<")
    with pytest.raises(ValueError):
        _struct.Struct("<b<b")
    with pytest.raises(ValueError):
        _struct.Struct("<b<b<b")
    with pytest.raises(ValueError):
        _struct.Struct("<b<b<b<b")
    with pytest.raises(ValueError):
        _struct.Struct("<b<b<b<b<b")
