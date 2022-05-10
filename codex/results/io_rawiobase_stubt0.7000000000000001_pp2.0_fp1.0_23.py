import io
class File(io.RawIOBase):
    def __init__(self, name, mode, buffering=0):
        # open the file
        self.file = open(name, mode, buffering)
        # call the base class method
        super(File, self).__init__()
    # read method
    def read(self, n=-1):
        return self.file.read(n)
    # write method
    def write(self, b):
        return self.file.write(b)
    # close method
    def close(self):
        return self.file.close()
    # tell method
    def tell(self):
        return self.file.tell()
    # seek method
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
# create the file object
f = File('file.txt', 'w+')
# write some data to the file
f.write(b"Hello World")
# seek to the start of the file
f.seek(0)
# read the contents of the file
print(f.read())
# close the
