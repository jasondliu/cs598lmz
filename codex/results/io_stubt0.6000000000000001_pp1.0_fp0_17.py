import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# PY-1086
import gzip

f = gzip.open(fileobj=io.BytesIO(b""))
f.read()
del f
f = gzip.open(fileobj=io.BytesIO(b""))
f.read1(1)
del f

# PY-1087
import gzip
f = gzip.open(fileobj=io.BytesIO(b""))
f.seek(1)
del f
f = gzip.open(fileobj=io.BytesIO(b""))
f.seek(1, 0)
del f
f = gzip.open(fileobj=io.BytesIO(b""))
f.seek(1, 1)
del f
f = gzip.open(fileobj=io.BytesIO(b""))
f.seek(1, 2)
del f

# PY-1088
import gzip
f = gzip.open(fileobj=io.BytesIO(b""))
f.tell()
del f
f = gzip.open(fileobj=io
