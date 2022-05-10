import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.buffer = b""
        self.buffer_size = 4096

    def read(self, size=-1):
        if size == -1:
            size = self.buffer_size
        if size > len(self.buffer):
            self.buffer += self.read_from_file(size - len(self.buffer))
        ret = self.buffer[:size]
        self.buffer = self.buffer[size:]
        return ret

    def read_from_file(self, size):
        with open(self.filename, "rb") as f:
            return f.read(size)

def gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

def gen_file(filename):
    with File(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line.strip()

def gen_file_mmap(filename):
    with open
