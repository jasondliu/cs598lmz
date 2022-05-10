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

del File
c = ''.join(map(chr, view[40:40+40]))
print(c)

del view
</code>
This generates the following output on CPython 3.6.2:
<code>&lt;class '__main__.File'&gt;&lt;class '__main__.File'&gt;&lt;c
</code>
As you can observe, even though <code>File</code> was deleted, it was in memory (I can see its type!), and <code>view</code> was referring to an object (for <code>view</code> was not <code>None</code>). I thought that a deleted object must be considered garbage and reclaimed, but apparently these objects are not garbage. Then what are they?

