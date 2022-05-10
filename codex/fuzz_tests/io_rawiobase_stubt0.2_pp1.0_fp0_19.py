import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.f = open(filename, 'rb')
        self.size = os.fstat(self.f.fileno()).st_size
    def read(self, size=-1):
        return self.f.read(size)
    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        self.f.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

def load_file(filename):
    with File(filename) as f:
        return f.read()

def load_file_as_string(filename):
    return load_file(filename).decode('utf-8')

def load_file_as_json(filename):
    return json.loads(load_file_as_string(filename))

def load_file_as_yaml(filename):
   
