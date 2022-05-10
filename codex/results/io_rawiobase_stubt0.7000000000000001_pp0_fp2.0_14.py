import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.encoding = 'utf-8'
    def read(self, count=-1):
        return self.file.read(count).decode(self.encoding)
    def write(self, string):
        return len(self.file.write(string.encode(self.encoding)))
    def readable(self):
        return True
    def writable(self):
        return True
</code>
EDIT:
I've decided to do it this way, but I don't know how to access the file's <code>encoding</code> attribute:
<code>class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.encoding = file.encoding
    def read(self, count=-1):
        return self.file.read(count).decode(self.encoding)
    def write(self, string):
        return len(self.file.write(string.encode(self.encoding)))
    def
