import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b'\x00' * n

f = File()
print(f.read(10))
# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# io.RawIOBase.readinto()
# readinto() reads data from the stream and stores it into a pre-allocated, writable bytes-like object b.
# The number of bytes read is returned, and the exact behaviour depends on the underlying implementation.
# If the object is a mutable sequence, the number of bytes read will be the length of b.
# If the object is a mutable bytearray, the number of bytes read will be the length of b,
# and the bytes object will be updated with the new data.
# If the object is an immutable bytes-like object, a bytes object of the same length as b will be returned,
# containing the data that was read.
# If the object is a writable buffer, the number of bytes read will be the length of b,
# and
