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
isinstance(io.FileIO(), io.FileIO)
isinstance(io.FileIO(), io.RawIOBase)
isinstance(io.FileIO(), io.IOBase)

# Test io.BufferedReader
isinstance(io.BufferedReader(io.FileIO()), io.BufferedReader)
isinstance(io.BufferedReader(io.FileIO()), io.BufferedIOBase)
isinstance(io.BufferedReader(io.FileIO()), io.IOBase)

# Test io.BufferedWriter
isinstance(io.Buff
