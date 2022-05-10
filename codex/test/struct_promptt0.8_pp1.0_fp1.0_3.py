import _struct
# Test _struct.Struct

St = _struct.Struct('hhl')

assert St.size == 8
St.format
St.pack(*range(3))
St.unpack(St.pack(*range(3))) == tuple(range(3))
# Test _struct.Struct object

st = St.build(*range(3))

def test_struct_object():
    assert st.size == 8
    st.format
    st.pack() == St.pack(*range(3))
    st.unpack(st.pack()) == tuple(range(3))
    st[:] == tuple(range(3))
    st == St.unpack(St.pack(*range(3)))
    st != (0, 1, 2)
    st.data

test_struct_object()
# Test _struct.Struct object slice

st_slice = st[:2]

def test_struct_object_slice():
    assert st_slice.size == 4
    st_slice.format
    st_slice.pack() == St.pack(*range(2))
