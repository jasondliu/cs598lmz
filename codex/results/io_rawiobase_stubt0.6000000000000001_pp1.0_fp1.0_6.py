import io
class File(io.RawIOBase):
    def __init__(self, data, mode='r'):
        self.data = data
        self.mode = mode
        self.pos = 0
    def read(self, size=-1):
        if size == -1:
            return self.data[self.pos:]
        else:
            data = self.data[self.pos:self.pos+size]
            return data
    def seek(self, pos, whence=0):
        if whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = len(self.data) + pos
        else:
            self.pos = pos
        return self.pos
    def tell(self):
        return self.pos
    def close(self):
        pass

def get_file_handle(file_name):
    with open(file_name, 'rb') as f:
        return File(f.read())

def get_file_handle_string(data):
    return File(data)

class PILImage(object):
    def __init__(self
