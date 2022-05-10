from lzma import LZMADecompressor
LZMADecompressor.ext_filter = bz2.BZ2Decompressor.ext_filter

class BadZipFile(zipfile.BadZipFile):
    pass

class ZipExtFile(io.BufferedIOBase):
    def __init__(self, fp, mode, compress_type, zinfo, *, closefp=True, password=None):
        self.fp = fp
        self.buffer = EMPTY_BUFFER
        self.mode = mode
        self.compress_type = compress_type
        self.zinfo = zinfo
        self.closefp = closefp
        self.password = password
        self.name = zinfo.orig_filename
        self.offset = 0
        self.decompressor = None
        if self.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
            raise RuntimeError('Bad compression type')
        if self.mode not in ('r', 'U', 'rU'):
            raise ValueError('open() requires mode `r`, `U` or `rU`')

