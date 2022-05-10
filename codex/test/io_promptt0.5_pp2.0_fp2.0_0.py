import io
# Test io.RawIOBase.readinto()

# test that readinto() returns the number of bytes read

import io
import os
import sys

# A mixin class that provides a read() method.
class Readable(object):
    def __init__(self, buf):
        self.buf = buf
        self.offset = 0
    def read(self, n=-1):
        if n < 0:
            n = len(self.buf) - self.offset
        self.offset += n
        return self.buf[self.offset - n:self.offset]

# A mixin class that provides a write() method.
class Writeable(object):
    def __init__(self):
        self.buf = []
    def write(self, s):
        self.buf.append(s)
    def flush(self):
        pass

# A mixin class that provides a seek() method.
class Seekable(object):
    def __init__(self):
        self.offset = 0
