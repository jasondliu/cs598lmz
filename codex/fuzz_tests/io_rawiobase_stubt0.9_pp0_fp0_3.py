import io
class File(io.RawIOBase):
    """
    file object for moving data in a multipart http request
    """

    def __init__(self, name, buffer=None):
        """
        init the object. The buffer argument is the initial
        data for the file object
        """
        self.name = name
        self.pos = 0
        self.ended = False
        if buffer:
            self.buffer = buffer

    def write(self, data):
        """
        write data to the file
        """
        self.pos += len(data)
        if 'buffer' not in self.__dict__:
            self.buffer = data[:]
        else:
            self.buffer += data[:]

    def read(self, size=-1):
        """
        read data from the file
        """
        if size == -1:
            buff = self.buffer[self.pos:]
            self.pos = len(self.buffer)
            return buff
        else:
            buff = self.buffer[self.pos:self.pos+size]
            self.pos += size
            return buff

    def
