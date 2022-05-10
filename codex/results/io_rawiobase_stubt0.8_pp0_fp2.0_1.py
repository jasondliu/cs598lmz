import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def read(self, *args):
        if self.file is None:
            self.file = open(self.filename, "rb")
        return self.file.read(*args)
</code>
Just an example, I'm not sure what all methods you need to provide. I think <code>seek()</code> is another one.

