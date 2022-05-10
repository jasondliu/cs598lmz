from bz2 import BZ2Decompressor
BZ2DecompressorMethod = BZ2Decompressor


class BZ2File(object):
    """Class to provide a file-like interface to a bz2 compressed file.

    Provides an interface similar to the Python 3 bz2.BZ2File class, but
    doesn't support context management.
    """

    def __init__(self, filename, mode="r", buffering=0x100000, compresslevel=1):
        """ filename: the filename to open
            mode: 'r' or 'w'
            buffering: ignored.
        """
        self.filename = filename
        self.closed = False
        self.mode = mode

        # simulate file attributes
        self.mode = mode
        self.name = filename
        self.encoding = None
        self.errors = None
        self.newlines = None

        if mode == "w":
            self._compressor = BZ2CompressorMethod(compresslevel)
            self._output = open(filename, "wb")
        elif mode == "r":
            self._decompressor = BZ2DecompressorMethod()

