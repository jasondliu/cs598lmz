import io
# Test io.RawIOBase
with io.FileIO(os.devnull, "r") as f:
    assert f.readinto(bytearray(1)) == 0

# Test io.BufferedIOBase
with io.BufferedReader(io.FileIO(os.devnull, "r")) as f:
    assert f.peek() == b""
    assert f.readline() == b""

# Test io.BytesIO
with io.BytesIO() as f:
    assert f.getvalue() == b""

# Test io.TextIOBase
with io.TextIOWrapper(io.FileIO(os.devnull, "r")) as f:
    assert f.read() == ""

# Test os.PathLike
with open(os.devnull) as f:
    assert f.read() == ""

# Test pathlib.Path
with pathlib.Path(os.devnull).open() as f:
    assert f.read() == ""

# Test posix io.FileIO
with io.FileIO(os.devnull, "wb") as f:
