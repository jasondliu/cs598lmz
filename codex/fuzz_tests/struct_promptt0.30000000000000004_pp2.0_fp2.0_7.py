import _struct
# Test _struct.Struct.

import _struct

def test_struct_format_size():
    # Test _struct.Struct.format_size()
    assert _struct.Struct('i').format_size() == 4
    assert _struct.Struct('ii').format_size() == 8
    assert _struct.Struct('i'*10).format_size() == 40
    assert _struct.Struct('i'*100).format_size() == 400
    assert _struct.Struct('i'*1000).format_size() == 4000
    assert _struct.Struct('i'*10000).format_size() == 40000
    assert _struct.Struct('i'*100000).format_size() == 400000
    assert _struct.Struct('i'*1000000).format_size() == 4000000
    assert _struct.Struct('i'*10000000).format_size() == 40000000
    assert _struct.Struct('i'*100000000).format_size() == 400000000
    assert _struct.Struct('i'*1000000000).format_size() == 4000000000
    assert _struct.Struct('i'
