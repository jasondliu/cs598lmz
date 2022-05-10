import io
# Test io.RawIOBase(io.IOBase)
# Test io.FileIO(io.RawIOBase)
# Test io.BufferedIOBase(io.IOBase)
# Test io.BufferedWriter(io.BufferedIOBase)
# Test io.BufferedReader(io.BufferedIOBase)
# Test io.BufferedRWPair(io.BufferedIOBase)
# Test io.TextIOBase(io.IOBase)
# Test io.TextIOWrapper(io.TextIOBase, io.BufferedIOBase)
# Test io.StringIO(io.TextIOBase)
# Test io.BytesIO(io.BufferedIOBase)

# test io.StringIO
def test_io_stringio():
    sio = io.StringIO('hello world', 'utf-8')
    assert isinstance(sio, io.StringIO)
    assert isinstance(sio, io.TextIOBase)
    assert isinstance(sio, io.BufferedIOBase)
    assert isinstance(sio, io.IOBase)
    assert sio.getvalue()
