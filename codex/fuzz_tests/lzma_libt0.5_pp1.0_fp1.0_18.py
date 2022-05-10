import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress
lzma_decompressobj = lzma.decompressobj
lzma_compressobj = lzma.compressobj

class LZMAFile(object):
    def __init__(self, filename, mode="r", format=None, check=-1, preset=None, filters=None):
        self.filename = filename
        self.mode = mode
        self.format = format
        self.check = check
        self.preset = preset
        self.filters = filters
        self.fileobj = None

    def open(self):
        if self.mode in ("r", "rb"):
            self.fileobj = lzma_decompressobj(self.filters)
            self.fileobj.check = self.check
        elif self.mode in ("w", "wb"):
            self.fileobj = lzma_compressobj(self.preset, self.filters)
        else:
            raise
