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
The output for the above code is <code>b'\x00'</code>. Is this intended?
It looks like <code>io.RawIOBase.readinto()</code> is defined to return a number of bytes read. Setting <code>view</code> in the <code>readinto()</code> implementation makes it look like <code>readinto()</code> is returning a value 0, but I don't think it is actually a return value.

