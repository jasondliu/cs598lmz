import io
# Test io.RawIOBase with the C implementation of io.BufferedRandom
from _io import BufferedRandom
import _io
f = io.BytesIO()
b = BufferedRandom(f)
b.write(b"hello")
b.seek(0)
b.read()
# Test io.IOBase with the C implementation of io.BufferedReader
f = io.BytesIO()
