import io
class File(io.RawIOBase):
    """Mock file object from an in-memory 'file'"""
    def __init__(self, file_path):
        self.pos = 0
        self.file_path = file_path
        self.fo = open(file_path, 'wb')
        self.closed = False
        self.name = file_path
        self.mode = 'wb'
    def read(self, size=-1):
        """Mock the read method"""
        return self.fo.read(size)
    def write(self, data):
        """Mock the write method"""
        self.fo.write(data)
        self.pos += len(data)
    def seek(self, offset):
        """Mock the seek method"""
        self.pos += offset
    def tell(self):
        """Mock the tell method"""
        return self.pos
    def flush(self):
        """Mock the flush method"""
        self.fo.flush()
    def close(self):
        """Mock the close method"""
        self.closed = True
    def seekable(
