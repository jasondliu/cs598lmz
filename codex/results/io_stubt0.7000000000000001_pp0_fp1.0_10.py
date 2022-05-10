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

class File2(io.RawIOBase):
    def readinto(self, buf):
        buf[0] = 0
    def readable(self):
        return True

f = io.BufferedReader(File2())
f.read(1)
del f
</code>
The first time I call <code>readinto</code>, <code>view</code> is <code>bytearray(b'\x00')</code>, which is correct.
The second time I call <code>readinto</code>, <code>view</code> is <code>bytearray(b'\x00')</code>, which is not correct.
Python 3.7.0 (default, Oct  2 2018, 08:59:49) 
[GCC 6.4.0] on linux

