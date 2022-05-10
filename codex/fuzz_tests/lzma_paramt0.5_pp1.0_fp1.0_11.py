from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, _: b""

class LzmaFile(object):
    def __init__(self, fileobj):
        self.fileobj = fileobj
        self.decompressor = LZMADecompressor()

    def read(self, size):
        return self.decompressor.decompress(self.fileobj.read(size))

    def __getattr__(self, name):
        return getattr(self.fileobj, name)

def lzmaopen(filename, mode="rb", fileobj=None):
    if "r" in mode:
        mode = mode.replace("r", "")
        fileobj = LzmaFile(fileobj if fileobj else open(filename, mode))
        return io.BufferedReader(fileobj)
    elif "w" in mode:
        mode = mode.replace("w", "")
        fileobj = fileobj if fileobj else open(filename, mode)
        return io.BufferedWriter(LzmaFile(fileobj))
    else:
        raise ValueError("Mode must include
