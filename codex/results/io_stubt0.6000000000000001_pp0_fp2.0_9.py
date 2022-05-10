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

# f is deleted, but buf is not
print(view[0])
</code>
The output is <code>10</code>, which I think is the <code>\n</code> character.
I found the <code>writable</code> method in the <code>io</code> module, but how can I do the same thing for reading?


A:

If you want to just read one character, then you can use <code>f.read1(1)</code> instead of <code>f.read(1)</code>.

