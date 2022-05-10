import io
class File(io.RawIOBase):
    def __init__(self):
        self.file = io.BytesIO()
        self.file.write(b'hello')
    def read(self, size = -1):
        return self.file.read(size)
    def readable(self):
        return True
</code>
I tested it with <code>open(File())</code> and I can't find anything wrong.

