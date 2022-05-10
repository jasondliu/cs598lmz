import _struct
# Test _struct.Struct

def test_struct():
    import sys
    import _struct
    st = _struct.Struct('hhl')
    sz = st.size
    print(sz)
    assert sz == 8
    # 'hhl' means two short ints and a long int.
    # 'bb' means two signed chars.
    # 'hh' means two net order (big endian) short ints.
    # 'iii' means three native order ints.
    # 'llh' means two little endian longs and a short.
    # '3s' means three chars, aka a string of length 3.
    # '10p' means a pointer to ten chars.
    # '10s' means a string of length 10.
    # 'P' means a pascal string, first byte is the length.
    # 'x' means one byte of padding.
    # 'cxh' means one byte of padding, one char and a short.
    # 'cb' means one signed char and one byte of padding.
    # 'bBhHiIlLqQfdspPx
