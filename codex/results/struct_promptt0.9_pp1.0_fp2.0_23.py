import _struct
# Test _struct.Struct with all possible combinations of endianness and
# alignment for 1, 2, 4, and 8 byte types.  All structure types should be
# tested at least once.

def get_conversion_table(byteorder, alignment):
    '''
    Given an endianness and alignment, return a sequence of tuples.
    Each tuple corresponds to a unique format string and contains
    a format string and the result of using st.unpack to unpack
    the resulting packed data.
    '''
    expected_results = []
    for i in range(1, 9):
        format = 'x' * i
        s = _struct.Struct(format)
        if byteorder == 'big':
            format = '>' + format
        elif byteorder == 'little':
            format = '<' + format
        st = _struct.Struct(format)
        b = bytes(range(1, i + 1))
        packed = s.pack(b)
        expected = st.unpack(packed)
        expected_results.append((format, expected))
    formats = [f for f, e
