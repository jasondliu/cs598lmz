import bz2
bz2.BZ2Compressor

class BZip2Compressor(object):
    def __init__(self, compresslevel=9):
        self.compresslevel = compresslevel
        self.compressor = None

    def compress(self, data):
        if self.compressor is None:
            self.compressor = bz2.BZ2Compressor(self.compresslevel)
        return self.compressor.compress(data)

    def flush(self):
        if self.compressor is not None:
            ret = self.compressor.flush()
            self.compressor = None
            return ret
        else:
            return ''

def bz2_compress(data, compresslevel=9):
    compressor = BZip2Compressor(compresslevel)
    return compressor.compress(data) + compressor.flush()

class BZip2Decompressor(object):
    def __init__(self):
        self.decompressor = None

    def decompress(self, data):
        if self.decompressor is None:
            self.dec
