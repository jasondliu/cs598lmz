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

f = io.BufferedReader(io.FileIO('/dev/null'))
print(f.read())
</code>
I get the following error:
<blockquote>
<p>TypeError: Required argument 'bytes' (pos 1) not found</p>
</blockquote>
Expected output:
<code>b''
</code>
Python version: 3.5.2

