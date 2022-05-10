import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readable(self):
        return True
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()

import sys
sys.modules[__name__]=File(sys.modules[__name__])

# Code to add an option to disable the print statement
# and the print() function.  This is not necessary for the
# rest of the script to work.

DISABLE_PRINT = True

if DISABLE_PRINT:

