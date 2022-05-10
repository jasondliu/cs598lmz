import _struct
# Test _struct.Struct.

# test _struct.Struct.__new__
with pytest.raises(TypeError) as excinfo:
    _struct.Struct()
assert str(excinfo.value) == "Struct() takes exactly 1 argument (0 given)"
with pytest.raises(TypeError) as excinfo:
    _struct.Struct(1, 2)
assert str(excinfo.value) == "Struct() takes exactly 1 argument (2 given)"
with pytest.raises(TypeError) as excinfo:
    _struct.Struct(1)
assert str(excinfo.value) == "first argument must be string"
with pytest.raises(TypeError) as excinfo:
    _struct.Struct(b"")
assert str(excinfo.value) == "first argument must be string"
with pytest.raises(TypeError) as excinfo:
    _struct.Struct(u"")
assert str(excinfo.value) == "first argument must be string"
with pytest.raises(TypeError) as excinfo:
    _struct.Struct("")
assert str(exc
