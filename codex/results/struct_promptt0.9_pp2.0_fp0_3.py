import _struct
# Test _struct.Struct with n != 1.
with struct.Struct("i") as s:
    s.pack_into(buf, 0, 1)
    assert _struct.Struct(s).unpack(buf)[0] == 1
    s.pack_into(buf, 0, 2)
    assert _struct.Struct(s).unpack(buf)[0] == 2
# Test _struct.Struct with string argument.
with struct.Struct("i") as s:
    s.pack_into(buf, 0, 123)
    assert _struct.Struct(s.format).unpack(buf)[0] == 123

# Test pack_into method.
with struct.Struct("i") as s:
    s.pack_into(buf, 0, 123)
    assert s.unpack(buf)[0] == 123
    with pytest.raises(TypeError) as excinfo:
        s.pack_into()
    assert 'pack_into() takes at least 3 arguments (0 given)' in str(excinfo.value)
    with pytest.raises(TypeError) as excinfo:
        s.
