import lzma
# Test LZMADecompressor

compressed = b"x\x9c\xab\x36\x0e\x00\x00\x10\x00\xff\xff"

decompressor = lzma.LZMADecompressor()
