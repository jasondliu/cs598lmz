import io
# Test io.RawIOBase
print('io.RawIOBase')
print(isinstance('hello world', io.RawIOBase))
print(isinstance(b'hello world', io.RawIOBase))
print(isinstance(io.BytesIO(), io.RawIOBase))
print(isinstance(io.StringIO(), io.RawIOBase))
print(isinstance(io.BufferedRWPair(io.BytesIO(b'hello'), io.BytesIO(b'world')), io.RawIOBase))
print(isinstance(io.BufferedRandom(io.BytesIO(b'hello')), io.RawIOBase))
print(isinstance(io.BufferedReader(io.BytesIO(b'hello')), io.RawIOBase))
print(isinstance(io.BufferedWriter(io.BytesIO()), io.RawIOBase))
print(isinstance(io.BufferedRWPair(io.BytesIO(b'hello'), io.BytesIO(b'world')), io.RawIOBase))
print(isinstance(io.BufferedRandom(io.BytesIO(b'hello')),
