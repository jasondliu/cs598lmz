import lzma
# Test LZMADecompressor

def read_all(dc, size):
    data = empty(size, dtype="B")
    have = 0
    while have < size:
        chunk = dc.decompress(data[have:])
        n = len(chunk)
        have += n
        if not n:
            raise EOFError("Not enough data")
    return data

def read_fh(dc, size, fh):
    data = empty(size, dtype="B")
    have = 0
    while have < size:
        chunk = dc.decompress(data[have:], size-have)
        n = len(chunk)
        have += n
        if not n:
            raise EOFError("Not enough data")
        fh.write(chunk)
    return data

# -- Test cases ---------------------------------------------------------------

class BaseCompressTestCase(unittest.TestCase):
    # Base class for compression test cases.

    compression = None # To be set in subclasses
    prefix = "BZh" # The typical prefix for the compression

    def
