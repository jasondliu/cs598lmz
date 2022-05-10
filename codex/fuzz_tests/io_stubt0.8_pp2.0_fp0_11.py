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

print(view[0])
</code>
If I run this code with Python 2.7.6 it will print <code>0</code>, but if I run it with Python 3.4.3 it will print <code>128</code> (i.e. the corresponding byte value).
The same happens if instead of <code>view[0]</code> I use <code>view[0] and 1</code> or the like.
Why this difference?
I'm using 64 bit versions of Python with the same version of Windows.

