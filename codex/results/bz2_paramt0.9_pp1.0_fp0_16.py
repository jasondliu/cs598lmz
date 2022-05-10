from bz2 import BZ2Decompressor
BZ2Decompressor()

#-------------------------------------------------------------------------------
class TarDecompressor(Decompressor):
    """A class to decompress a tar.bz2 compressed file."""
#-------------------------------------------------------------------------------
# Constructor
    def __init__(self):
        """A constructor that performs the decompression steps."""
        super().__init__()
        self._logger.debug("Opening the source file: %s.", self._source)
        source = open(self._source, "rb")
        self._dest = self._dest.replace(".tar.gz", "")
        mkpath(self._dest)
        self._logger.debug("Decompressing the source file: %s.", self._source)
        with tarfile.open(fileobj=source, mode="r|gz") as tar:
            tar.extractall(self._dest)
        self._logger.debug("Closing the source file: %s.", self._source)
        source.close()
