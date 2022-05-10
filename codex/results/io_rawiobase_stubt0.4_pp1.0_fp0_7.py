import io
class File(io.RawIOBase):
    """
    Wrapper around the file-like object returned by the
    :meth:`~zipfile.ZipFile.open` method of :class:`ZipFile`.
    """
    def __init__(self, zf, mode, zinfo,
                 close_fd=True, pwd=None,
                 compress_type=None,
                 *,
                 force_zip64=False):
        self._zf = zf
        self._close_fd = close_fd
        self._compress_type = compress_type
        self._pwd = pwd
        self._force_zip64 = force_zip64
        self._zinfo = zinfo
        self._compressor = None
        self._decompressor = None
        self._decompressor_for_read = None
        self._readbuffer = None
        self._offset = 0
        self._universal = 'U' in mode
        self._mode = mode
        self._did_close = False

        if self._mode in ('r', 'rU'):
            self._decompressor = self._z
