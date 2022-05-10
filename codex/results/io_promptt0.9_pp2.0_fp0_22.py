import io
# Test io.RawIOBase.readinto()

bs = io.BytesIO(bytes('Hello World!\n', 'ascii'))
raw = io.BufferedRandom(bs)
buf = bytearray('X', 'ascii')

buf = raw.readinto(buf)
buf = bytearray('X'*256, 'ascii')  # There's no way for us to know how many bytes were read
n = raw.readinto(buf)
assert n == len(buf)

# Cannot read beyond the end of file
buf = bytearray(1, 'ascii')
n = raw.readinto(buf)
assert n == 0

# Invalid types
try:
    raw.readinto(1)
    assert False
except TypeError:
    pass
try:
    raw.readinto(u'abc')
    assert False, 'no unicode buffer'
except TypeError:
    pass
else:
    import array
    raw.readinto(array.array('i', 1))

# io.RawIOBase.readinto1()
raw =
