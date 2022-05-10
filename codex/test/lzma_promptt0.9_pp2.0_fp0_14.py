import lzma
# Test LZMADecompressor

class Myfile(object):
    def __init__(self, filename):
        self.filename = filename

    def read(self, bytes=None):
        # See the docs of lzma.open() for why func should return bytes
        with open(self.filename, 'rb') as fp:
            s = fp.read()
        return s

