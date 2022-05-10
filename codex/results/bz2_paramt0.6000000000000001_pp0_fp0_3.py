from bz2 import BZ2Decompressor
BZ2Decompressor()

class BZ2File(file):
    """
    BZ2File(filename[, mode[, buffering]]) -> file object

    Open a bzip2-compressed file in binary or text mode, returning
    a file object.
    """

    def __init__(self, filename, mode="r", buffering=0):
        file.__init__(self, filename, mode, buffering)
        if self.mode in ("r", "rb"):
            self.decompressor = BZ2Decompressor()
            self.read = self._read_with_bz2
        else:
            self.decompressor = None
            self.write = self._write_with_bz2

    def _read_with_bz2(self, size=-1):
        # size parameter is ignored
        data = file.read(self, 1024)
        if not data:
            return ""
        return self.decompressor.decompress(data)

    def _write_with_bz2(self, data):
        raise NotImplementedError
