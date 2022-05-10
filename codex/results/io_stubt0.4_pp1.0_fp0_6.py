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
</code>
I'm getting <code>None</code> as the output. I'm expecting <code>b'\x00'</code>. I'm not sure why the buffer is not being filled.


A:

The <code>readinto</code> method of <code>io.RawIOBase</code> is supposed to return the number of bytes read.  You're not returning anything, so it's returning <code>None</code>.

