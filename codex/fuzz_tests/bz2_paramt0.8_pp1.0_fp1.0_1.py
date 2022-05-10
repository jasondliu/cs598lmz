from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor()

class GzipReader(FileReader):
    def __init__(self, filename):
        FileReader.__init__(self, filename)
        self.gzf = gzip.GzipFile(filename)

    def get_name(self):
        return self.gzf.name

    def read(self):
        return self.gzf.read()

class BZ2Reader(FileReader):
    def __init__(self, filename):
        FileReader.__init__(self, filename)
        self.bzf = bz2.BZ2File(filename)

    def get_name(self):
        return self.bzf.name

    def read(self):
        return self.bzf.read()

class Reader(object):
    def __init__(self, filename):
        self.real_name = filename
        self.filename = filename

        if filename.endswith(".gz"):
            self.name = filename[:-3]
            self.obj = GzipReader(filename)

       
