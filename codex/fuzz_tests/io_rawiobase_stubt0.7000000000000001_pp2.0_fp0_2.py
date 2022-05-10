import io
class File(io.RawIOBase):
    """
    Mock class for io.FileIO
    """
    def close(self):
        pass

class FileIO(io.BufferedIOBase):
    """
    Mock class for io.FileIO
    """
    def close(self):
        pass
