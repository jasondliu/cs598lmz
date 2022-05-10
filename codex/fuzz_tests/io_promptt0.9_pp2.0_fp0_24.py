import io
# Test io.RawIOBase.readinto() 
# io.RawIOBase.readinto(dst, /) reads size bytes from the stream and into a writable buffer dst
# dst must be writable bytes-like object (e.g. bytes, bytearray...)

in_buf1 = bytearray(b'*' * 10)     # A writable buffer pre-filled with *
in_buf2 = bytearray(b'*' * 10)     # Likewise

indata = b'0123456789abcdef'       # Binary test data

in_buf1.extend(b'*' * 10)          # Extend the buffer to fill it
print(in_buf1)                     # bytearray(b'**********')
in_buf2.extend(b'*' * 10)          # Likewise
print(in_buf2)                     # bytearray(b'**********')

instream = io.BytesIO(indata)      # A readable binary stream

# Read at most 10 bytes from the stream, readjust the buffer's data, and return the number of
