from lzma import LZMADecompressor
LZMADecompressor(format = FORMAT_AUTO, memlimit = MEMLIMIT_DEFAULT, filters = None)

class LZMADecompressionBuffer:
    """This is a buffer that decompresses lzma on the fly and outputs the
    decompressed file. It's a context manager so you can use it with the "with"
    statement.
    
    It is based on the implementation of the LZMACompressionBuffer class by David
    Cournapeau, from the Python 2.7 documentation."""
    
    def __init__(self, fileobj, format = FORMAT_AUTO, memlimit = MEMLIMIT_DEFAULT, filters = None):
        self.fileobj = fileobj
        self.decompressor = LZMADecompressor(format, memlimit, filters)
        self.pos = 0
        self.unused_data = b''
    
    def __getattr__(self, name):
        return getattr(self.fileobj, name)
    
    def read(self, size = -1):
        """Read up to size uncompressed bytes from
