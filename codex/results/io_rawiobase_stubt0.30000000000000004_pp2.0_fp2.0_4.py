import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.f = open(path, "rb")
        self.size = os.fstat(self.f.fileno()).st_size

    def read(self, size=-1):
        return self.f.read(size)

    def seek(self, offset, whence=io.SEEK_SET):
        return self.f.seek(offset, whence)

    def tell(self):
        return self.f.tell()

    def close(self):
        return self.f.close()

def get_file_size(path):
    return os.fstat(open(path, "rb").fileno()).st_size

def get_file_hash(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

def get_file_hash_from_file(f):
    return hashlib.sha256(f.read()).hexdigest()

def get_file_hash_from_file_object(f):

