import io
# Test io.RawIOBase
assert isinstance(io.RawIOBase(), io.RawIOBase)
assert not isinstance(io.RawIOBase(), io.IOBase)

# Test io.BufferedIOBase
assert isinstance(io.BufferedIOBase(), io.BufferedIOBase)
assert not isinstance(io.BufferedIOBase(), io.IOBase)
assert not isinstance(io.BufferedIOBase(), io.RawIOBase)

# Test io.TextIOBase
assert isinstance(io.TextIOBase(), io.TextIOBase)
assert not isinstance(io.TextIOBase(), io.IOBase)
assert not isinstance(io.TextIOBase(), io.RawIOBase)
assert not isinstance(io.TextIOBase(), io.BufferedIOBase)
# Test io.FileIO
assert isinstance(io.FileIO(__file__, 'r'), io.FileIO)
assert isinstance(io.FileIO(__file__, 'r'), io.IOBase)
assert not isinstance(io.FileIO(__file__, 'r'), io.RawIOBase)
