import _struct
# Test _struct.Struct.__new__().

_struct.Struct.__new__(_struct.Struct)

try:
    _struct.Struct.__new__(_struct.Struct, format='')
except TypeError:
    pass
else:
    raise TestFailed


# Test _struct.Struct.format().

st = _struct.Struct('hhl')

if st.format != 'hhl':
    raise TestFailed

try:
    st.format = 'h'
except AttributeError:
    pass
else:
    raise TestFailed


# Test _struct.Struct.size().

st = _struct.Struct('hhl')

if st.size != 8:
    raise TestFailed

try:
    st.size = 6
except AttributeError:
    pass
else:
    raise TestFailed


# Test _struct.Struct.pack().

st = _struct.Struct('hhl')

