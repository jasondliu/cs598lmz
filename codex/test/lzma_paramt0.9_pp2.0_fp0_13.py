from lzma import LZMADecompressor
LZMADecompressor()
del LZMADecompressor

try:
    from lzma import LZMADecompressor
except ImportError:
    pass
