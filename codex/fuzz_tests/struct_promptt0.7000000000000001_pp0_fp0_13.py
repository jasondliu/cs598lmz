import _struct
# Test _struct.Struct(format).unpack(buffer)
from test import test_support
from test.test_support import bigaddrspacetest

test_support.requires('largefile')
test_support.bigaddrspacetest = bigaddrspacetest

def test_unpack():
    import _struct
    st = _struct.Struct('hhl')
    buf = 'abcd' + '\0'*8
    assert st.unpack(buf) == (25185, 25699, 16909060)

def test_unpack_from():
    import _struct
    st = _struct.Struct('hhl')
    buf = 'abcd' + '\0'*8
    assert st.unpack_from(buf, 2) == (25699, 16909060)
    assert st.unpack_from(buffer(buf, 2), 0) == (25699, 16909060)

def test_pack_into():
    import _struct
    st = _struct.Struct('hhl')
    buf = bytearray('abcd' + '\0'*8)

