import io
# Test io.RawIOBase & io.BufferedIOBase inheritance
assert issubclass(io.RawIOBase, io.IOBase)
assert issubclass(io.BufferedIOBase, io.IOBase)
# Test BufferedReader & BufferedWriter inheritance
assert issubclass(io.BufferedReader, io.BufferedIOBase)
assert issubclass(io.BufferedWriter, io.BufferedIOBase)
# Test BufferedRWPair inheritance
assert issubclass(io.BufferedRWPair, io.BufferedIOBase)
# Test TextIOBase inheritance
assert issubclass(io.TextIOBase, io.IOBase)
# Test TextIOWrapper inheritance
assert issubclass(io.TextIOWrapper, io.TextIOBase)
# Test IncrementalNewlineDecoder inheritance
assert issubclass(io.IncrementalNewlineDecoder, io.IncrementalDecoder)
# Test FileIO inheritance
assert issubclass(io.FileIO, io.RawIOBase)
# Test BytesIO inheritance
assert issubclass(io.BytesIO, io.BufferedIOBase)
