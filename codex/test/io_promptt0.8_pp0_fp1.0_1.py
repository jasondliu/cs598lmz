import io
# Test io.RawIOBase
assert isinstance(io.RawIOBase(), io.RawIOBase)
# Test io.BytesIO
assert isinstance(io.BytesIO(), io.BytesIO)
# Test io.StringIO
assert isinstance(io.StringIO(), io.StringIO)
# Test io.BufferedIOBase
assert isinstance(io.BufferedIOBase(), io.BufferedIOBase)
# Test io.BufferedReader
assert isinstance(io.BufferedReader(io.BytesIO()), io.BufferedReader)
# Test io.BufferedWriter
assert isinstance(io.BufferedWriter(io.BytesIO()), io.BufferedWriter)
# Test io.BufferedRWPair
