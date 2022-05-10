import io
# Test io.RawIOBase 
class FileIO(io.IOBase):

    def __init__(self, file, mode='r'):
        if mode not in ('r', 'w'):
            raise ValueError("mode must be 'r' or 'w'")
        self.mode = mode
        # here open() is where the file actually gets opened
        self._file = io.FileIO(file, mode)

