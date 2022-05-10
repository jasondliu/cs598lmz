import io
# Test io.RawIOBase
print("io.RawIOBase")
f = io.BytesIO()
print("io.RawIOBase.read() = %s" % f.read())
print("io.RawIOBase.readinto() = %s" % f.readinto(bytearray(1)))
print("io.RawIOBase.readall() = %s" % f.readall())
print("io.RawIOBase.write() = %s" % f.write(b'abc'))
print("io.RawIOBase.fileno() = %s" % f.fileno())
print("io.RawIOBase.seekable() = %s" % f.seekable())
print("io.RawIOBase.readable() = %s" % f.readable())
print("io.RawIOBase.writable() = %s" % f.writable())
print("io.RawIOBase.seek() = %s" % f.seek(1))
print("io.RawIOBase.tell() = %s" % f.tell())
print("io.RawIOBase.flush() = %s
