from lzma import LZMADecompressor
LZMADecompressor.decompress(compressed_data).decode('utf-8')
 
# decompress
compressed_data = b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00'
decompressor = LZMADecompressor()
decompressor.decompress(compressed_data)
decompressor.decompress(b'')
decompressor.flush()

# decompress
compressed_data = b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00'
decompressor = LZMADecompressor()
decompressor.decompress(compressed_data)
decompressor.unused_data
decompressor.unconsumed
