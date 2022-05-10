import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f

    def read(self, n=-1):
        return self.f.read(n)

    def write(self, b):
        n = self.f.write(b)
        return n

    def seekable(self):
        return self.f.seekable()

    def seek(self, offset, whence=io.SEEK_SET):
        self.f.seek(offset, whence)

    def tell(self):
        return self.f.tell()

    def readable(self):
        return self.f.readable()

    def writable(self):
        return self.f.writable()

    def close(self):
        self.f.close()

import csv
def csv_reader(file_obj):
    csv_reader = csv.reader(file_obj, delimiter=',')
    for row in csv_reader:
        if row:
            print(" ".join(row))

with open("data/iris.csv") as f:
    c
