import io
class File(io.RawIOBase):
    """
    This class will represent a file in memory.
    """
    def __init__(self, filename):
        """
        Constructor.
        :param filename: name of the file.
        """
        self.filename = filename
        self.file = None
        self.buffer = None

    def __enter__(self):
        """
        Open the file.
        :return: self
        """
        self.file = open(self.filename, 'rb')
        self.buffer = self.file.read()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the file.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.file.close()

    def read(self, n=-1):
        """
        Read a number of bytes from the file.
        :param n: number of bytes to read.
        :return: bytes read from the file.
        """
        if n
