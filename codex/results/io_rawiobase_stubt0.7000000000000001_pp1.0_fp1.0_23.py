import io
class File(io.RawIOBase):
    def __init__(self, path):
        super(File, self).__init__()
        self._file = open(path, "rb")
        self.path = path

    def close(self):
        self._file.close()

    def read(self, size):
        return self._file.read(size)

    def readable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)

    def seekable(self):
        return True

    @property
    def closed(self):
        return self._file.closed

    @property
    def name(self):
        return self.path

def get_file(path):
    return File(path)

def get_file_size(path):
    return os.path.getsize(path)

def binary_to_json(path, mode='r'):
    with open(path, mode=mode) as f:
        return json.load(f)

def json_to_binary(obj
