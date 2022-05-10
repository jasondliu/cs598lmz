from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = lambda self, data: bz2.decompress(data)

from bz2 import BZ2Compressor
BZ2Compressor.compress = lambda self, data: bz2.compress(data)

from bz2 import BZ2File
BZ2File.__init__ = lambda self, filename, mode, compresslevel=9, fileobj=None: bz2.BZ2File.__init__(self, filename, mode, compresslevel, fileobj)
BZ2File.close = lambda self: bz2.BZ2File.close(self)
BZ2File.flush = lambda self: bz2.BZ2File.flush(self)
BZ2File.fileno = lambda self: bz2.BZ2File.fileno(self)
BZ2File.isatty = lambda self: bz2.BZ2File.isatty(self)
BZ2File.next = lambda self: bz2.BZ2File.next(self)
BZ2File.read = lambda self,
