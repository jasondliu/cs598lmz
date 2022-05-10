import bz2
# Test BZ2Decompressor

d = bz2.BZ2Decompressor()

d.decompress(b'BZh91AY&SY')

d.decompress(b'A')

d.decompress(b'\x00\x00\x00\x01\x00')

d.decompress(b'\x00\x00\x00\x01\x01')

d.decompress(b'\x00\x00\x00\x01\x02')

d.decompress(b'\x00\x00\x00\x01\x03')

d.decompress(b'\x00\x00\x00\x01\x04')

d.decompress(b'\x00\x00\x00\x01\x05')

d.decompress(b'\x00\x00\x00\x01\x06')

d.decompress(b'\x00\x00\x00\x01\x07')

d
