import io
class File(io.RawIOBase):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'rb')
        self.fd = self.file.fileno()
        self.offset = 0

    def __del__(self):
        self.file.close()

    def readinto(self, b):
        data = os.read(self.fd, len(b))
        b[:len(data)] = data
        self.offset += len(data)
        return len(data)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = os.stat(self.file_path).st_size - offset
        return self.offset

def get_puzzle_data(file_path):
    file = open(file_path, 'r')
    puzzle_data = [int(line
