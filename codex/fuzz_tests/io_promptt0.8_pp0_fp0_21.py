import io
# Test io.RawIOBase with in the context manager
with io.BytesIO() as bio:
    # Test write() separately since read1() will only work after data is written first.
    bio.write(b"a")
    assert bio.seek(0) == 0
    assert bio.read1(1) == b"a"
    assert bio.seek(0) == 0
    assert bio.read1(2) == b"a"

# Test io.RawIOBase with in the context manager
with io.BytesIO() as bio:
    bio.write(b"a")
    # Test read() separately since readinto1() will only work after data is written first.
    data = bytearray(b"bb")
    assert bio.readinto1(data) == 1
    assert data == b"ab"

# Test io.RawIOBase with in the context manager
with io.BytesIO() as bio:
    bio.write(b"a")
    # Test read() separately since read1() will only work after data is written first.
    assert bio.read() == b"a"


