import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\x00' * 5) == b'\x00' * 3

decompressor.decompress(b'') == b''  # Not done yet
decompressor.unused_data == b''

decompressor.decompress(b'\x00' * 20) == b'\x00' * 16
decompressor.unused_data  # Not done yet

decompressor.decompress(b'\xff') == b''
decompressor.unused_data == b'\xff'

decompressor.decompress(b'\xc0', max_length=9) == b'\x00' * 9
decompressor.unused_data == b''

decompressor.decompress(b'\x00' * 4, max_length=2) == b'\x00' * 2
decompressor.unused_data == b'\x00' * 2

decompressor.decompress
