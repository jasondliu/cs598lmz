import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

########################################################################
class Zstd:
    """
    The Zstd compression module.
    """
    #----------------------------------------------------------------------
    def __init__(self):
        """"""
        self.name = "zstd"
        self.extension = ".zst"
        self.has_extension = True
        self.is_compressed = True
        self.compresslevel = 5
        self.compress = zstd_compress
        self.decompress = zstd_decompress
        
########################################################################
class Lzma:
    """
    The Lzma compression module.
    """
    #----------------------------------------------------------------------
    def __init__(self):
        """"""
        self.name = "lzma"
        self.extension = ".lzma"
        self.has_extension = True
        self.is_compressed = True
        self.compresslevel = 9
        self.compress = lzma_
