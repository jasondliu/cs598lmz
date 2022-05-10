import io
class File(io.RawIOBase):
    def __init__(self, file_path, mode='rb', buffering=0, encoding=None, errors=None, newline=None,
                 closefd=True, opener=None):

        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline

        if opener is not None:
            if closefd:
                flags = os.O_RDONLY
            else:
                flags = os.O_RDWR

            if hasattr(os, 'O_BINARY'):
                flags |= os.O_BINARY
            fd = opener(file_path.encode("utf-8"), flags)
        else:
            fd = os.open(file_path, os.O_RDONLY | os.O_BINARY)

        super(File, self).__init__(file_descriptor=fd)
fd = open("mytest.txt", "rb")
file_data = fd.read()
fd.close()
print(file_data)


