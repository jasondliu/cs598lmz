import io
# Test io.RawIOBase
isinstance(io.RawIOBase(), io.RawIOBase)
isinstance(io.RawIOBase(), io.IOBase)
# Test io.BufferedIOBase
isinstance(io.BufferedIOBase(), io.BufferedIOBase)
isinstance(io.BufferedIOBase(), io.IOBase)
# Test io.TextIOBase
isinstance(io.TextIOBase(), io.TextIOBase)
isinstance(io.TextIOBase(), io.IOBase)

# Test io.FileIO
