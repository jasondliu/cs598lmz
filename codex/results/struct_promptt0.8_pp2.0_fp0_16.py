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
    else:
        raise AssertionError, "Struct didn't raise TypeError"

# Check basic structure
check_struct(_struct.Struct('x'), 'x', 0, 0, 0)
check_struct(_struct.Struct('xy'), 'xy', 1, 1, 2)
check_struct(_struct.Struct('xyz'), 'xyz', 2, 2, 3)
check_struct(_struct.Struct('x  y  z  '), 'x  y  z  ', 2, 2, 3)
check_struct(_struct.Struct('x\ty\
