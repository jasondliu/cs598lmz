import io
class File(io.RawIOBase):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.current_position = 0
        self.file_size = os.path.getsize(self.file_name)

    def read(self, size=-1):

        if size == -1:
            size = self.file_size
        if size + self.current_position >= self.file_size:
            size = self.file_size - self.current_position
        with open(self.file_name, 'rb') as f:
            f.seek(self.current_position)
            part = f.read(size)
            self.current_position += size
            return part

    def tell(self):
        return self.current_position

    def seek(self, position, whence=0):
        if whence == 0:
            self.current_position = position
        elif whence == 1:
            self.current_position += position
        elif whence == 2:
            self.current_position = self.file_size
