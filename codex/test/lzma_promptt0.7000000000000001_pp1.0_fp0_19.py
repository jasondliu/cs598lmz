import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

def decompress(compr):
    with lzma.open(compr,'rb') as fh:
        return fh.read()

# Usage:
