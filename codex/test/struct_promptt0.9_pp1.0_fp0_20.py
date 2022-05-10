import _struct
# Test _struct.Struct('double').format argument.
def test_format_double():
    expected = 'd'
    actual = _struct.Struct('double').format
    assert actual == expected
