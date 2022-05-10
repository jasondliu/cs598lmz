import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
    def read(self, size=0):
        with open(self.path, 'rb') as f:
            return f.read(size)
    def tell(self):
        return self.f.tell()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def close(self):
        return self.f.close()
</code>
I'm not sure how to use it, though. I tried:
<code>import io
import os

with open('/data/test.png', 'rb') as f:
    reader = png.Reader(file=f)
    res = reader.read()
</code>
but <code>Reader</code> expects a <code>png.File</code> object, not a <code>io.RawIOBase</code> object. Passing <code>f</code> directly doesn't work either.
How do I use the <code>png.Reader</code> without loading the file into memory?


