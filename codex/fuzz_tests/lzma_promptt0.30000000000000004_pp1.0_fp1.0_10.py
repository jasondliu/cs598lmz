import lzma
# Test LZMADecompressor

data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

decompressor = lzma.LZMADecompressor()
decompressor.decompress(data)

decompressor.unused_data

decompressor.eof

decompressor.decompress(b'')

decompressor.unused_data

decompressor.eof

decompressor.decompress(b'\x00\x00\x00\x00')

decompressor.unused_data

decompressor.eof

decompressor.decompress(b'\x00\x00\x00\x00')

decompressor.unused_data

decompressor.eof

# Test LZMADecompressor.flush()

decompressor = lzma
