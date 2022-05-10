import _struct
# Test _struct.Struct

import _struct

def test_struct_format():
    # Check that format string is validated
    raises(TypeError, _struct.Struct, 0)
    raises(TypeError, _struct.Struct, 0, 0)
    raises(TypeError, _struct.Struct, "")
    raises(TypeError, _struct.Struct, "", 0)
    raises(TypeError, _struct.Struct, "x")
    raises(TypeError, _struct.Struct, "x", 0)
    raises(TypeError, _struct.Struct, "x", 1)
    raises(TypeError, _struct.Struct, "x", 1, 0)
    raises(TypeError, _struct.Struct, "x", 1, 0, 0)
    raises(TypeError, _struct.Struct, "x", 1, 0, 0, 0)
    raises(TypeError, _struct.Struct, "x", 1, 0, 0, 0, 0)
    raises(TypeError, _struct.Struct, "x", 1, 0, 0, 0, 0, 0)
    raises(TypeError, _struct
