import bz2
# Test BZ2Decompressor

d = bz2.BZ2Decompressor()

d.decompress(b'BZh91AY&SY')

d.decompress(b'A')

d.decompress(b'\x00\x00\x00\x01\x00')

