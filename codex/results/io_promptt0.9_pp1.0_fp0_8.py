import io
# Test io.RawIOBase:
io.RawIOBase.readinto()
# Test io.RawIOBase:
io.RawIOBase.readinto2()
# Test io.RawIOBase:
io.RawIOBase.readline()
# Test io.BytesIO:
# Test io.BytesIO.readinto:
io.FileIO('abcd', 'r')
# Test io.BufferedIOBase:
bio = io.BufferedIOBase()
bio.peek()
bio.peek(1)
bio.peek(1, 2)
# Test io.IOBase:
io.IOBase()
# Test io.BufferedIOBase.__index__:
index = bio.__index__()
str(index)
# Test io.BufferedIOBase.__length_hint__:
len(bio)
# Test io.BufferedIOBase.fileno:
bio.fileno()
# Test io.BufferedIOBase.isatty:
io.BufferedIOBase().isatty()
# Test io.BufferedIOBase.readable:
io.
