import io
# Test io.RawIOBase.readinto()
r = io.BytesIO(b"What's up doc?")
buf = bytearray(7)
n = r.readinto(buf)
buf
 
s = io.StringIO("What's up doc?")
buf = bytearray(7)
n = r.readinto(buf)
buf
# Test io.RawIOBase.seek()
r = io.BytesIO(b"What's up doc?")
r.tell()
r.seek(4)
r.tell()
buf = bytearray(7)
n = r.readinto(buf)
buf
n = r.readinto(buf)
buf
try:
    r.seek(8, io.SEEK_CUR)
except io.UnsupportedOperation:
    pass
