import _struct
# Test _struct.Struct objects
def check_struct(st, format, size, alignment, packed=0):
    assert isinstance(st, _struct.Struct)
    assert st.format == format
    assert st.size == size
    assert st.alignment == alignment
    assert st.pack('x') == 'x' * packed

def check_struct_error(st, format, size, alignment, packed=0):
    try:
        check_struct(st, format, size, alignment, packed)
    except AssertionError:
        pass
