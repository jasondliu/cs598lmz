import io
class File(io.RawIOBase):
    """An object providing a file-like interface to a file in a zipfile.
    """
    def __init__(self, zipfile, zinfo, mode="r", pwd=None):
        zipfile.fp.seek(zinfo.header_offset, 0)
        self._fileobj = zipfile.fp
        self._zipfile = zipfile
        self._zinfo = zinfo
        self._decrypter = None
        self._close_fileobj = False
        if mode not in ("r", "U", "rU"):
            raise RuntimeError('open() requires mode "r", "U", or "rU"')
        if pwd and not zinfo.flag_bits & 0x1:
            raise RuntimeError('File %r is not encrypted' % zinfo.filename)
        if zinfo.flag_bits & 0x20:
            mode = mode.replace('U', '')
        self._mode = mode
        self._pwd = pwd
        self._readbuffer = b''
        self._offset = 0
        self._decrypter = _Zip
