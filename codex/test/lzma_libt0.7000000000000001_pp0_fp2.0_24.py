import lzma
lzma.open

class LZMAFile(object):
    """
    File-like object that reads from LZMA-compressed data.
    """

    # This class is largely identical to bz2.BZ2File, but it uses lzma instead
    # of bz2.
    # This is an implementation of lzma in pure Python.
    # http://www.joachim-bauch.de/projects/lzma-pure-python/

    def __init__(self, filename=None, mode="r",
                 fileobj=None, compresslevel=9):
        if mode not in ("r", "rb"):
            raise ValueError("mode must be 'r' or 'rb'")

        if filename is None and fileobj is None:
            raise ValueError("filename or fileobj must be given")

        if filename is not None and fileobj is not None:
            raise ValueError("filename and fileobj may not both be given")

        if compresslevel < 1 or compresslevel > 9:
            raise ValueError("compresslevel must be between 1 and 9")
