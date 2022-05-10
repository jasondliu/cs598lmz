import io
class File(io.RawIOBase):
    """
    A file-like object that reads from a file in the zipfile.
    """
    def __init__(self, zipfile, zinfo, mode="r",
                 pwd=None, *, force_zip64=False):
        self._zipfile = zipfile
        self._filePassed = False
        self._decrypter = None
        self._compress_type = zinfo.compress_type
        self._compress_left = zinfo.compress_size
        self._left = zinfo.file_size
        self._eof = False
        self._pos = 0
        self._offset = zinfo.header_offset
        self._unicodeFilename = zinfo.filename
        self._decode_extra = zinfo._decode_extra
        self._fileRefCnt = 1
        self._pwd = pwd
        self._compress_type = zinfo.compress_type
        self._compress_left = zinfo.compress_size
        self._left = zinfo.file_size
        self._eof = False

