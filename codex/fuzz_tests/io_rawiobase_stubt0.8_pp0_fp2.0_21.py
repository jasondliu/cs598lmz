import io
class File(io.RawIOBase):
    """
    Serial communication with a file object interface.
    Intended for testing, it does not simulate data transfer or
    serial line errors.
    """

    def __init__(self, path):
        """
        Create a new file serial communicator

        :param path: Path to the file to write to.
        """
        self.path = path
        self.file = open(path, 'a+t')

    def read(self, size=0):
        self.file.seek(0)
        return self.file.read(size)

    def write(self, data):
        self.file.write(data.decode('latin-1'))
        self.file.flush()

    def reset_input_buffer(self):
        self.file.seek(0)

    def close(self):
        self.file.close()
