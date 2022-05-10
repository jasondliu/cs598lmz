import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
d.decompress(b'\xfd[H\x9dV\x03\xfe\x00')

d = lzma.LZMADecompressor()
d.decompress(b'\xfd[H\x9dV\x03\xfe\x01ab')
b'ab'

