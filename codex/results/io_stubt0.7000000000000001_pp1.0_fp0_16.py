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
</code>
I know it's not a good idea to use <code>del</code>, but I want to know what happens.
When I run the following code:
<code>f = io.BufferedReader(File())
f.read(1)
del f
print(view)
</code>
the result is <code>b''</code>.
But when I run it by adding this code:
<code>f = io.BufferedReader(File())
f.read(1)
print(view)  # I added this line.
del f
print(view)
</code>
the result is <code>b'\x00'</code>.
So I think when I add <code>print(view)</code> line, the <code>view</code> data is not freed.
Why this happens?

