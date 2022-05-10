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
print(view)

# io.BytesIO

import io

f = io.BytesIO(b"abc")
f.read(1)
del f

# io.StringIO

import io

f = io.StringIO("abc")
f.read(1)
del f

# io.TextIOWrapper

import io

f = io.TextIOWrapper(io.BytesIO(b"abc"))
f.read(1)
del f

# io.BufferedRandom

import io

f = io.BufferedRandom(io.BytesIO())
f.read(1)
del f

# io.BufferedRWPair

import io

f = io.BufferedRWPair(io.BytesIO(), io.BytesIO())
f.read(1)
del f

# io.BufferedWriter

import io

f = io.BufferedWriter(io.BytesIO())
f.write(b"abc")
del f

# io.BufferedReader

import io

f = io
