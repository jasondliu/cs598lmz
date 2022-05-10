from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor()

class LZMAFile:
    """Allows reading from a binary lzma file"""

    def __init__(self, filename_or_filelike):
        """Open file or filelike object as stream."""
        if isinstance(filename_or_filelike, str):
            self.file = open(filename_or_filelike, 'rb')
        elif hasattr(filename_or_filelike, 'read'):
            self.file = filename_or_filelike
        else:
            raise ValueError('Filename has to be a str or the object must implement read()')
        self.decompressor = LZMADecompressor()

    def read(self, size=None, up_to=False):
        """Try to return size compressed bytes or whole file.

        Return less only if EOF or up is reached."""
        data = self._read_member()
        return data.read(size, up_to)

    def readlines(self):
        """Return all lines of current member, inclusive line endings."""
        data =
