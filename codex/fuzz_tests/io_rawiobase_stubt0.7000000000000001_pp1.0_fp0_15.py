import io
class File(io.RawIOBase):
    """
    A file like object that is backed by a file
    """
    def __init__(self, f):
        self.f = f

    def write(self, data):
        """
        Writes the data to the file
        """
        self.f.write(data)

    def close(self):
        """
        Closes the file
        """
        self.f.close()

class InMemoryFile(io.RawIOBase):
    """
    A file like object that is backed in memory
    """
    def __init__(self):
        self.data = b''

    def write(self, data):
        """
        Writes the data to the file
        """
        self.data += data

    def getvalue(self):
        """
        Returns the contents of the file
        """
        return self.data
