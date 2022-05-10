import bz2
# Test BZ2Decompressor's __del__ (before exit, or after __exit__)
# by running in a sub-process, so we can catch the exception.
# This is to bypass the exception handler in pythonrun.c.

script = """if 1:
    import io
    import struct
    import sys

    defbug = sys.gettrace()
    sys.settrace(None)

    # using buffered input to reproduce the problem
    eof = 0
    class Input:
        def __init__(self, data):
            self.data = data
            self.i = 0

        def read(self, n=-1):
            if self.i == len(self.data):
                return ""
            if n == -1:
                res, self.i = self.data[self.i:], len(self.data)
            else:
                res, self.i = self.data[self.i:self.i+n], min(self.i+n, len(self.data))
            return res

    # read-only file-like object that throws EOFError after
    # it has
