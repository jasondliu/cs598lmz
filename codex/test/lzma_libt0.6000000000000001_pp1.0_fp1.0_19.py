import lzma
lzma.LZMAError

class LZMAFile(object):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        if self.mode == 'r':
            self.fileobj = lzma.LZMAFile(self.filename, mode=self.mode)
        elif self.mode == 'w':
            self.fileobj = lzma.LZMAFile(self.filename, mode=self.mode, format=lzma.FORMAT_ALONE, filters=[{"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME}])
        return self.fileobj

    def __exit__(self, exc_type, exc_value, traceback):
        self.fileobj.close()

class LZMAError(Exception):
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
