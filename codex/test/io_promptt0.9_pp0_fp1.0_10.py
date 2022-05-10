import io
# Test io.RawIOBase
print(io.RawIOBase.seekable.__doc__)
print(io.RawIOBase.tell.__doc__)
print(io.RawIOBase.fileno.__doc__)

raw = io.RawIOBase()
print(raw.isatty())

raw._checkClosed()

# Test io.RawIOBase
print(io.RawIOBase.read.__doc__)
print(io.RawIOBase.readall.__doc__)
print(io.RawIOBase.readinto.__doc__)
