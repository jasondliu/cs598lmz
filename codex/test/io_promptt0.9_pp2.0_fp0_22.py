import io
# Test io.RawIOBase.readinto()

bs = io.BytesIO(bytes('Hello World!\n', 'ascii'))
raw = io.BufferedRandom(bs)
buf = bytearray('X', 'ascii')

buf = raw.readinto(buf)
buf = bytearray('X'*256, 'ascii')  # There's no way for us to know how many bytes were read
n = raw.readinto(buf)
