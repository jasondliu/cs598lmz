import lzma
# Test LZMADecompressor accepts a bytes-like object.
LZMADecompressor().decompress(b'\x5d\x00\x00')
# Test LZMADecompressor accepts a memoryview.
LZMADecompressor().decompress(memoryview(b'\x5d\x00\x00'))
# Test LZMADecompressor accepts a bytearray.
LZMADecompressor().decompress(bytearray(b'\x5d\x00\x00'))
# Test incremental_decoder accepts a bytes-like object.
incremental_decoder(None, b'\x5d\x00\x00')
# Test incremental_decoder accepts a memoryview.
incremental_decoder(None, memoryview(b'\x5d\x00\x00'))
# Test incremental_decoder accepts a bytearray.
incremental_decoder(None, bytearray(b'\x5d\x00\x00'))
