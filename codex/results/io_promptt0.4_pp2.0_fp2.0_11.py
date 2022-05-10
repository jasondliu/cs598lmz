import io
# Test io.RawIOBase
with open('/dev/tty', 'rb') as f:
    assert isinstance(f, io.RawIOBase)
    assert f.readable()
    assert not f.writable()
    assert not f.seekable()
    assert not f.isatty()
    assert f.fileno() > 0
    assert f.read(1) == b'\x03'
    assert f.read(1) == b'\x04'
    assert f.read(1) == b'\x05'
    assert f.read(1) == b'\x06'
    assert f.read(1) == b'\x07'
    assert f.read(1) == b'\x08'
    assert f.read(1) == b'\x09'
    assert f.read(1) == b'\x0a'
    assert f.read(1) == b'\x0b'
    assert f.read(1) == b'\x0c'
    assert f.read(1) == b'\x0d'

