import lzma
# Test LZMADecompressor.__init__
decompressor = lzma.LZMADecompressor()
# Test LZMADecompressor.decompress
data = b"x\x9cK\xcb\xcf\x07\r\xc9\xcf/\xcaI\x01\x00\x04\x80\x0f\x00\x00\x00"
