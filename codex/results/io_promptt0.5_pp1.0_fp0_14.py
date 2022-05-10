import io
# Test io.RawIOBase
print('Test io.RawIOBase')
rawIOBase = io.RawIOBase()
print(rawIOBase.read(1))
print(rawIOBase.readinto(b'\x00'))
print(rawIOBase.readinto1(b'\x00'))
print(rawIOBase.readall())
print(rawIOBase.read1(1))
print(rawIOBase.write(b'123'))
rawIOBase.seek(1)
print(rawIOBase.tell())
rawIOBase.truncate(1)
rawIOBase.close()
print(rawIOBase.fileno())
print(rawIOBase.isatty())
print(rawIOBase.readable())
print(rawIOBase.seekable())
print(rawIOBase.writable())
print()

# Test io.RawIOBase
print('Test io.RawIOBase')
rawIOBase = io.RawIOBase()
print(rawIOBase.read(1))
print(rawIOBase.readinto(b'\x00'))
print(rawIO
