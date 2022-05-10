import _struct
# Test _struct.Struct

def test_struct_creation():
    st = _struct.Struct('i')
    assert st.size == 4
    assert st.format == 'i'

    st = _struct.Struct('ii')
    assert st.size == 8
    assert st.format == 'ii'

    st = _struct.Struct('iii')
    assert st.size == 12
    assert st.format == 'iii'

    st = _struct.Struct('iiii')
    assert st.size == 16
    assert st.format == 'iiii'

    st = _struct.Struct('iiiii')
    assert st.size == 20
    assert st.format == 'iiiii'

    st = _struct.Struct('iiiiii')
    assert st.size == 24
    assert st.format == 'iiiiii'

    st = _struct.Struct('iiiiiii')
    assert st.size == 28
    assert st.format == 'iiiiiii'

    st = _struct.Struct('iiiiiiii')
    assert st.size == 32
    assert st.format == 'iiii
