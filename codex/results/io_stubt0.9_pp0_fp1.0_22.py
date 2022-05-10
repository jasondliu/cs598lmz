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
sys.getrefcount(view)
</code>
The output is <code>1</code>, proving that the <code>BufferedReader</code> has been destroyed and has released the reference.
If you have a problem where this happens though, it must be related to something else in your code.
For instance, if you do this...
<code>f = io.BufferedReader(File())
a = f.read(1)
b = f.read(1)
del f
sys.getrefcount(view)
</code>
... then it will still show <code>1</code> in the memory view because the inner <code>BytesIO</code> will still be around (the <code>BufferedReader</code> maintains a reference to it for the next read), but if you do this...
<code>f = io.BufferedReader(File())
a = f.read(1)
b = f.read(1)
c = f.read(1)
del f
sys.getrefcount(view)
</code>
then the output will be <code>2</code> because
