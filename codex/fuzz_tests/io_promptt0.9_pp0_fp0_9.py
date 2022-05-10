import io
# Test io.RawIOBase with direct access
rawio = io.RawIOBase(open(b'io_raw.py', 'rb'))
fileio = io.FileIO(b'io_raw.py', 'rb')

assert rawio.readable()
assert rawio.readinto(bytearray(4)) == 4
assert rawio.tell() == 4
assert rawio.seek(0, io.SEEK_SET) == 0
assert rawio.readinto(bytearray(1)) == 1
assert rawio.seek(0, io.SEEK_CUR) == 1
assert rawio.readinto(bytearray(1)) == 1
assert rawio.seek(0, io.SEEK_END)
assert rawio.tell() == io.DEFAULT_BUFFER_SIZE
assert rawio.fileno() == 0xbadf00
assert rawio.isatty()
try:
    rawio.truncate()
    assert False, "Should have thrown"
except io.UnsupportedOperation:
    pass
assert rawio.readable()
assert not rawio.writ
