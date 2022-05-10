import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\x00' * 5) == b'\x00' * 3

decompressor.decompress(b'') == b''  # Not done yet
decompressor.unused_data == b''

decompressor.decompress(b'\x00' * 20) == b'\x00' * 16
decompressor.unused_data  # Not done yet

