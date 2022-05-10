import _struct
# Test _struct.Struct

import struct

def test_struct():
    # 0-length struct
    st = _struct.Struct('')
    assert st.size == 0
    assert st.pack() == b''
    assert st.pack_into(bytearray()) == 0
    assert st.unpack(b'') == ()
    assert st.unpack_from(b'') == ()

    # 1-char struct
    st = _struct.Struct('c')
    assert st.size == 1
    assert st.pack(b'a') == b'a'
    assert st.unpack(b'a') == (b'a',)
    assert st.unpack_from(b'a') == (b'a',)
    assert st.unpack_from(b'ab') == (b'a',)
    b = bytearray(b'ab')
    st.pack_into(b, 1, b'c')
    assert b == b'abc'
    assert st.unpack_from(b, 1) == (b'c',)

    #
