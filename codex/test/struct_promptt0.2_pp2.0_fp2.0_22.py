import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('z')
    except TypeError:
        pass
