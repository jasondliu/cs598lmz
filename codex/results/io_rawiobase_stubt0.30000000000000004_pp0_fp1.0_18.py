import io
class File(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
    def open(self):
        self.file = open(self.file_path, 'rb')
    def read(self, size=-1):
        return self.file.read(size)
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

class FileReader(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
        self.file_size = 0
        self.file_offset = 0
        self.file_chunk_size = 0
        self.file_chunk_offset = 0
        self.file_chunk = None
    def open(self):
        self.file = open(self.file_path, 'rb')
        self.file_size = os.path.getsize(self.file_path)
        self.file_offset = 0

