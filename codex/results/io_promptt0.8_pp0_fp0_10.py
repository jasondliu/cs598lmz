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
b = BufferedReader(f)
b.write(b"hello")
b.seek(0)
b.read()
# Test io with the C implementation of io.BufferedWriter
f = io.BytesIO()
b = BufferedWriter(f)
b.write(b"hello")
b.seek(0)
b.read()
# Test _io with the C implementation of _io.BufferedRWPair
f = io.BytesIO()
b = BufferedRWPair(f, f)
b.write(b"hello")
b.seek(0)
b.read()
# Test _io with the C implementation of _io.BufferedRandom
f = io.BytesIO()
b = Buff
