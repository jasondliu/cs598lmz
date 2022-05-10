import io
# Test io.RawIOBase(bytes) with invalid arguments
with pytest.raises(TypeError):
    io.RawIOBase()
with pytest.raises(TypeError):
    io.RawIOBase('b')
with pytest.raises(TypeError):
    io.RawIOBase(b'b', None)
with pytest.raises(TypeError):
    io.RawIOBase(b'b', 'c')
with pytest.raises(ValueError):
    io.RawIOBase(b'b', 'w')
with pytest.raises(TypeError):
    io.RawIOBase(b'b', 'w', None)
with pytest.raises(TypeError):
    io.RawIOBase(b'b', 'w', 42)
