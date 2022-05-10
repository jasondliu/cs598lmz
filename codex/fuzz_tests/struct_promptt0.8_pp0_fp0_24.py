import _struct
# Test _struct.Struct

def test_Struct():
    integer_code = 'i'
    float_code = 'f'
    double_code = 'd'

    # A struct unpack should consume all the input data
    s = _struct.Struct('iii')
    if platform.python_implementation() == 'CPython':
        assert s.size == 12
    result = s.unpack(integer_code * 12)
    assert len(result) == 3
    assert result == (0, 0, 0)

    # If the input is too short, an error should be raised
    with pytest.raises(struct.error) as excinfo:
        s.unpack('i' * 10)
    assert excinfo.value.args[0] == 'unpack requires a bytes object of length 12'

    # A struct pack should return all the bytes
    packed_data = s.pack(1, 2, 3)
    assert len(packed_data) == len(integer_code) * 3
    assert packed_data == integer_code * 3

    # Check that format strings are not mutable
    with
