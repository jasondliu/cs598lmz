import io
# Test io.RawIOBase
with open('/dev/null', 'rb') as f:
    assert isinstance(f, io.RawIOBase)
    assert f.readable()
    assert not f.writable()
    assert not f.seekable()
with open('/dev/null', 'wb') as f:
    assert isinstance(f, io.RawIOBase)
    assert not f.readable()
    assert f.writable()
    assert not f.seekable()
with open('/dev/null', 'r+b') as f:
    assert isinstance(f, io.RawIOBase)
    assert f.readable()
    assert f.writable()
    assert not f.seekable()
with open('/dev/null', 'rb+') as f:
    assert isinstance(f, io.RawIOBase)
    assert f.readable()
    assert f.writable()
    assert not f.seekable()
with open('/dev/null', 'w+b') as f:
    assert isinstance(f, io.RawIOBase)
    assert f.readable()
