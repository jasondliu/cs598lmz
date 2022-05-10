import _struct
# Test _struct.Struct read function

import io
import sys

from support import bigendian

def cleanup(func, *args):
    return func(*args)

class bytesIO(io.BytesIO):
    def __init__(self, *args):
        io.BytesIO.__init__(self, *args)
        self.close_called = False

    def close(self):
        self.close_called = True
        io.BytesIO.close(self)
        return False

class bytesInIO(bytesIO):
    def readable(self):
        return True

class bytesOutIO(bytesIO):
    def writable(self):
        return True

try:
    import mmap
    class MemoryMappedIO(mmap.mmap):
        def __init__(self, *args):
            """MemoryMappedIO(fd, length=0, flags=mmap.MAP_SHARED,
                             prot=mmap.PROT_READ|mmap.PROT_WRITE,
                             access=mmap.ACCESS_DEFAULT[, offset=0
