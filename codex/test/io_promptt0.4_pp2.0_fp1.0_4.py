import io
# Test io.RawIOBase.readinto()

import _io

def readinto_helper(b, n):
    b[0] = ord('x')
    return n

