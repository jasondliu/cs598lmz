import io
# Test io.RawIOBase inheritance
type(io.BufferedReader(io.BytesIO()))
# Test io.BufferedIOBase inheritance
type(io.BufferedReader(io.BytesIO()).raw)
# Test io.TextIOBase inheritance
type(io.TextIOWrapper(io.BytesIO()))
# Test io.TextIOBase inheritance
type(io.TextIOWrapper(io.BytesIO()).buffer)
# Test io.BufferedRandom inheritance
type(io.BufferedReader(io.BytesIO()))
# Test io.FileIO inheritance
type(io.FileIO('/tmp/foo', mode='w'))
# Test io.BufferedWriter inheritance
type(io.BufferedWriter(io.BytesIO()))
# Test io.BufferedWriter inheritance
type(io.BufferedWriter(io.BytesIO()).raw)
# Test io.BufferedRWPair inheritance
type(io.BufferedRWPair(io.BytesIO(), io.BytesIO()))
# Test io.BufferedRWPair inheritance
