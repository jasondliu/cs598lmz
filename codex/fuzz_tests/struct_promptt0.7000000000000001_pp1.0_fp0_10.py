import _struct
# Test _struct.Struct.

def test_Struct():

    import sys
    import _struct
    if sys.byteorder == 'big':
        byteorder = '>'
    else:
        byteorder = '<'

    assert _struct.Struct('cbhilfd').format == byteorder + 'cbhilfd'

    s = _struct.Struct('cbhilfd')
    assert s.size == _struct.calcsize('cbhilfd')
    assert s.format == byteorder + 'cbhilfd'
    assert s.unpack('\0\1\1\1\1\1\1\1\1\1') == (0, '\x01', 1, 257, 65537,
                                             65537.0, 1.0)

    raises(OverflowError, s.unpack, '\0\1\1\1\1\1\1\1\1\1\1')

    s = _struct.Struct(byteorder + 'b')
    assert s.unpack('\xff') == (-1,)
    assert s.unpack('\x
