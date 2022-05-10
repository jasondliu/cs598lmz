import io
# Test io.RawIOBase
with open('/dev/null', 'r') as f:
    assert isinstance(f, io.RawIOBase)
# Test io.BufferedIOBase
with open('/dev/null', 'rb') as f:
    assert isinstance(f, io.BufferedIOBase)
# Test io.TextIOBase
with open('/dev/null', 'r') as f:
    assert isinstance(f, io.TextIOBase)
# Test io.IOBase
with open('/dev/null', 'r') as f:
    assert isinstance(f, io.IOBase)
# Test io.FileIO
with open('/dev/null', 'r') as f:
    assert isinstance(f, io.FileIO)
# Test io.BytesIO
with io.BytesIO() as f:
    assert isinstance(f, io.BytesIO)
# Test io.StringIO
with io.StringIO() as f:
    assert isinstance(f, io.StringIO)
# Test io.TextIOWrapper
with io.StringIO() as f:
