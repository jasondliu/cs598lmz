import io
class File(io.RawIOBase):
    """
    Represents a file-based module file.
    Uses the Python stdlib's io.FileIO to open the file
    """
    def __init__(self,
