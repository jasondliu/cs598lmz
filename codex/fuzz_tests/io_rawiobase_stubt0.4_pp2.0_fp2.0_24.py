import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.file = io.open(filename, mode)
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def write(self, b):
        return self.file.write(b)
    def readable(self):
        return self.file.readable()
    def seekable(self):
        return self.file.seekable()
    def writable(self):
        return self.file.writable()

def open(filename, mode='r'):
    if mode == 'r':
        return File(filename, mode)
    else:
        raise NotImplementedError
</code>
Now you can do:
<code>import io
import myfile

with io.open(myfile.open('my
