import lzma
lzma.LZMAError

class LZMAFile:
    def __init__(self, f, mode="r",
                 format=lzma.FORMAT_AUTO, check=-1, preset=None, filters=None):
        self.mode = mode
        self.name = getattr(f, "name", None)
        self.f = f
        if "r" in mode:
            self.lz = lzma.LZMADecompressor(format, check, None, None, filters)
            self.decompress = self.lz.decompress
        else:
            self.lz = lzma.LZMACompressor(format, check, preset, filters)
            self.compress = self.lz.compress
            self.flush = self.lz.flush

    def read(self, size=-1):
        if size < 0:
            return self.decompress()
        else:
            return self.decompress(self.f.read(size))

    def readinto(self, b):
        data
