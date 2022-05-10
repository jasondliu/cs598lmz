import io
class File(io.RawIOBase):
    """
    Class that wraps a file and behaves like a socket.
    """
    def __init__(self, file):
        super(File, self).__init__()
        self.file = file

    def recv(self, *args):
        return self.file.read(*args)

    def send(self, data):
        self.file.write(data)
        return len(data)

    def fileno(self):
        return self.file.fileno()

class StringIO(io.RawIOBase):
    """
    Class that wraps a string and behaves like a socket.
    """
    def __init__(self, string):
        super(StringIO, self).__init__()
        self.string = string
        self.pos = 0

    def recv(self, *args):
        data = self.string[self.pos:self.pos + args[0]]
        self.pos += len(data)
        return data

    def send(self, data):
        self.string += data
        return len(data)

    def fil
