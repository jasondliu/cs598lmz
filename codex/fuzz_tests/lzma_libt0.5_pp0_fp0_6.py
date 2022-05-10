import lzma
lzma.LZMAFile

import sys

class LZMAFile(lzma.LZMAFile):
    def __init__(self, filename, mode="r", *args, **kwargs):
        if not hasattr(filename, "read"):
            filename = open(filename, mode)
        self.filename = filename
        self.mode = mode
        lzma.LZMAFile.__init__(self, filename, mode, *args, **kwargs)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if not self.filename.closed:
            self.filename.close()

class LZMAStream(lzma.LZMAStream):
    def __init__(self, filename, mode="r", *args, **kwargs):
        if not hasattr(filename, "read"):
            filename = open(filename, mode)
        self.filename = filename
        self.mode = mode
        lzma.LZMAStream
