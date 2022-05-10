import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f, File
print(view)
</code>
This prints <code>bytearray(b'')</code> as expected. If I comment out the <code>del</code> statement, however, I get a <code>SystemError: error return without exception set</code> at the <code>print</code> line.
Why?
(Python 3.7.1 64bit on Windows 7)
Edit: I also tried to write my own <code>RawIOBase</code> implementation to see if I'm doing something wrong, but I get the same error:
<code>class File(io.RawIOBase):
    def readinto(self, buf):
        print(buf)
        return 1

f = io.BufferedReader(File())
f.read(1)
del f, File
</code>


A:

This is a bug in CPython and has been fixed in Python 3.7.6rc1 and Python 3.8.0b1.

