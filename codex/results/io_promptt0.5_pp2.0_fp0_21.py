import io
# Test io.RawIOBase

# Test basic operation
f = io.RawIOBase()
f.read(1)
f.readinto(bytearray(1))
f.readinto(memoryview(bytearray(1)))
f.readinto(array.array('b', [0]))
f.readinto(array.array('b', [0]), 0, 1)
f.readinto(bytearray(1), 0, 1)
f.readinto(memoryview(bytearray(1)), 0, 1)
f.write(b"")
f.write(bytearray(b""))
f.write(memoryview(b""))
f.seek(0)
f.tell()
f.close()

# Test default implementations
f = io.RawIOBase()
f.readable()
f.writable()
f.seekable()
f.fileno()
f.isatty()
f.readall()
f.read1(1)
f.readline()
f.readlines()
f.readinto1(bytearray(
