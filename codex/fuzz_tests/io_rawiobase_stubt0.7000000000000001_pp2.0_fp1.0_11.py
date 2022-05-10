import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.open()
    def open(self):
        self.file = io.open(self.file_name, self.mode, buffering=0)
    def close(self):
        self.file.close()
    def seek(self, offset, whence):
        self.file.seek(offset, whence)
    def tell(self):
        self.file.tell()
    def read(self, size):
        return self.file.read(size)
    def write(self, data):
        return self.file.write(data)
    def __del__(self):
        self.close()

def set_fmode(path, mode):
    os.chmod(path, mode)

def get_fmode(path):
    return os.stat(path).st_mode

def get_fsize(path):
    return os.stat(path).st_size

def set_ftime(path, time
