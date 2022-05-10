import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = None

    def open(self):
        self.file = open(self.path)

    def read(self, size=-1):
        return self.file.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)

    def tell(self):
        return self.file.tell()

    def close(self):
        self.file.close()

file = File('file.txt')
file.open()
file.read()
file.seek(10)
file.tell()

# You can also use the io.FileIO class to create file objects.
# This class is a subclass of RawIOBase and provides a raw stream for file objects.
# You can use the constructor of this class to create file objects.
# The constructor of the class takes two arguments:
#     The first argument is the name of the file.
#     The second argument is the mode in which the file is opened.
file =
