import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, size=-1):
        return open(self.name, 'rb').read(size)
    def write(self, b):
        open(self.name, 'wb').write(b)
    def close(self):
        pass

def get_file(name):
    return File(name)

def get_file_size(name):
    return os.path.getsize(name)

def get_file_stat(name):
    return os.stat(name)

def get_file_mtime(name):
    return os.path.getmtime(name)

def get_file_atime(name):
    return os.path.getatime(name)

def get_file_ctime(name):
    return os.path.getctime(name)

def get_file_owner(name):
    return os.path.getowner(name)

def get_file_group(name):
    return os.path.getgroup
