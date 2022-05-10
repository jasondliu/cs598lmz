import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except TypeError:
        pass
