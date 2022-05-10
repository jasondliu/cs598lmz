import io
class File(io.RawIOBase):
    def __init__(self, path):
        self._f = open(path, "rb")
    def read(self, size=-1):
        return self._f.read(size)
    def seekable(self):
        return self._f.seekable()
    def seek(self, offset, whence=io.SEEK_SET):
        return self._f.seek(offset, whence)
    def tell(self):
        return self._f.tell()
    def close(self):
        self._f.close()

def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

def get_file_size(file_path):
    with open(file_path, 'rb') as fp:
        fp.seek(0, os.SEEK_END)
        return fp.tell()

def get_file_name(file_path):
    return os.path.basename(file_path)

def get_file_path(file_path):
