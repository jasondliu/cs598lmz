import mmap

class Map(object):
    def __init__(self, filename, access=mmap.ACCESS_WRITE):
        self.filename = filename
        self.file_obj = open(filename, "r+b")
        self.map = mmap.mmap(self.file_obj.fileno(), 0, access=access)

    def __del__(self):
        self.close()

    def close(self):
        if self.map:
            self.map.close()
            self.map = None
        if self.file_obj:
            self.file_obj.close()
            self.file_obj = None

    def size(self):
        return self.map.size()

    def read(self, offset, size):
        self.map.seek(offset)
        return self.map.read(size)

    def write(self, offset, data):
        self.map.seek(offset)
        self.map.write(data)

    def flush(self):
        self.map.flush()

    def seek(self, offset):
