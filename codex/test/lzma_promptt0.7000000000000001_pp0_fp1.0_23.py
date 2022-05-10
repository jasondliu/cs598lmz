import lzma
# Test LZMADecompressor
from lzma import LZMADecompressor

def decompress(data):
    decompress = LZMADecompressor()
    return decompress.decompress(data)

