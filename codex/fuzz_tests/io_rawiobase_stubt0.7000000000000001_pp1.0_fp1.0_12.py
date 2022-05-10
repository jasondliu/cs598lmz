import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n).encode("utf-8")

class Tee(object):
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
    def write(self, data):
        self.file1.write(data)
        self.file2.write(data)
    def flush(self):
        self.file1.flush()
        self.file2.flush()
</code>

