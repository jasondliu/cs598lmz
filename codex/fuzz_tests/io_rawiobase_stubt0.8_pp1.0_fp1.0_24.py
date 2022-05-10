import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.name = filename
        self.f = open(filename, "rb")
        self.is_read = False
        self.size = os.path.getsize(filename)
        self.current_pos = 0
    def read(self, length = -1):
        if length == 0:
            return bytes()
        length = min(length, self.size - self.current_pos)
        if length == 0:
            return bytes()
        self.is_read = True
        self.current_pos += length
        return self.f.read(length)
    def close(self):
        self.f.close()
    def write(self, obj):
        raise NotImplementedError

class FileList(list):
    def __init__(self):
        list.__init__(self)
    def append(self, obj):
        f = File(obj)
        list.append(self, f)
        return f
    def diff(self):
        if len(self) == 0:
           
