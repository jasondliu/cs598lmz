import lzma
# Test LZMADecompressor Object
# it does not support context manager (__enter__, __exit__ methods)
ld = lzma.LZMADecompressor()

