import _struct
# Test _struct.Struct

def test_struct_format_size():
    # Test _struct.Struct.format_size()
    s = _struct.Struct("hhl")
    assert s.format_size("<") == 8
    assert s.format_size(">") == 8
    assert s.format_size("!") == 8
    assert s.format_size("=") == 8
    assert s.format_size("@") == 8
    assert s.format_size("<@") == 8
    assert s.format_size(">=") == 8
    assert s.format_size("!=") == 8
    assert s.format_size("@=") == 8
    assert s.format_size("@!") == 8
    assert s.format_size("@<") == 8
    assert s.format_size("@>") == 8
    assert s.format_size("<@=") == 8
    assert s.format_size(">@=") == 8
    assert s.format_size("!@=") == 8
