from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = lambda self, data: bz2.decompress(data)

from bz2 import BZ2Compressor
BZ2Compressor.compress = lambda self, data: bz2.compress(data)

from bz2 import BZ2File
BZ2File.read = lambda self, size: bz2.decompress(self.file.read(size))
BZ2File.write = lambda self, data: self.file.write(bz2.compress(data))

from bz2 import BZ2Compressor
BZ2Compressor.flush = lambda self: None
BZ2Compressor.close = lambda self: None

from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self: None
BZ2Decompressor.close = lambda self: None

from bz2 import BZ2File
BZ2File.close = lambda self: None
BZ2File.flush = lambda self: None

class BZ2_Stream(object):
    def __init__(
