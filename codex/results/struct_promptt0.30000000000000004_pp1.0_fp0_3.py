import _struct
# Test _struct.Struct

def test_struct_error():
    # Issue #17094: Struct() constructor should raise a TypeError if
    # the format string is not a string.
    with pytest.raises(TypeError):
        _struct.Struct(None)

def test_struct_error_2():
    # Issue #17094: Struct() constructor should raise a TypeError if
    # the format string is not a string.
    with pytest.raises(TypeError):
        _struct.Struct(42)

def test_struct_error_3():
    # Issue #17094: Struct() constructor should raise a TypeError if
    # the format string is not a string.
    with pytest.raises(TypeError):
        _struct.Struct(b"")

def test_struct_error_4():
    # Issue #17094: Struct() constructor should raise a TypeError if
    # the format string is not a string.
    with pytest.raises(TypeError):
        _struct.Struct(bytearray(b""))

def test_struct_
