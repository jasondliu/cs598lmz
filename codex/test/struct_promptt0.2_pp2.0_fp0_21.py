import _struct
# Test _struct.Struct.

def test_struct_format():
    # Test that the format string is checked for validity.
    try:
        _struct.Struct('x')
    except ValueError:
        pass
