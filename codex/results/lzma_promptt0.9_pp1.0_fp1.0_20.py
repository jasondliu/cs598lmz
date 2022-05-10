import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
d.decompress(b'\xfd[H\x9dV\x03\xfe\x00')

d = lzma.LZMADecompressor()
d.decompress(b'\xfd[H\x9dV\x03\xfe\x01ab')
b'ab'

d.decompress(b'\x01cde')
b'cde'

d.decompress(b'\x01fgh')
b'fgh'

d.decompress(b'\x02ij')
b'ij'

d.decompress(b'\x01klm')
b'klm'

d.decompress(b'\x03n')
b'n'

d.decompress(b'\x01opq')
b'opq'

d.decompress(b'')
b''

d.decompress(b'\x00')
b''


