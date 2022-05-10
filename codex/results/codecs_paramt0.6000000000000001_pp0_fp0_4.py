import codecs
codecs.register_error("strict", codecs.ignore_errors)

class ChunkReader(object):
    """
    A file-like object that reads chunks of data from a file.  This is
    useful when reading files that are too large to fit in memory.
    """

    def __init__(self, filename, chunksize=None, encoding="utf-8", errors="strict"):
        self.filename = filename
        self.chunksize = chunksize
        self.encoding = encoding
        self.errors = errors

        self.fileobj = open(filename, "rb")
        self.eof = False

    def read(self, chunksize=None):
        if self.eof:
            return ""

        if chunksize is None:
            chunksize = self.chunksize

        data = self.fileobj.read(chunksize)
        if not data:
            self.eof = True
            return ""

        return data.decode(self.encoding, self.errors)


class ChunkWriter(object):
    """
    A file-like object that writes chunks
