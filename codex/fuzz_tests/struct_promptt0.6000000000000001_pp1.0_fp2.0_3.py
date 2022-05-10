import _struct
# Test _struct.Struct() and .pack()

# To check the result of .pack(), we unpack the result to bytes using
# the same format, and check the result is the same as the original
# input.

def check(format, values, expected_result=None, expected_size=None):
    s = _struct.Struct(format)
    result = s.pack(*values)
    if expected_result is not None:
        assert result == expected_result
    if expected_size is not None:
        assert s.size == expected_size
    if expected_result is not None:
        assert result == expected_result
    assert s.unpack(result) == values
    b = bytearray()
    s.pack_into(b, 0, *values)
    assert s.unpack_from(b, 0) == values
    assert s.unpack(bytes(b)) == values
    assert s.unpack_from(bytes(b), 0) == values

def check_error(format, values, expected_exception):
    s = _struct.Struct(format)
    try
