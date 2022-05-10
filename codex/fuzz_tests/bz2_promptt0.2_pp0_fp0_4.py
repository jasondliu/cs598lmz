import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
d = bz2.BZ2Decompressor()
d.decompress(data)

# Test BZ2Decompressor.flush()

d = bz2.BZ2Decompressor()
d.decompress(data)
d.flush()

# Test BZ2Decompressor.decompress()

d = bz2.BZ2Decompressor()
d.decompress(data)
d.decompress(b'\x00\x00\x00\x01\x01')

# Test BZ2Decompressor.unused_data

d = bz2.BZ2Decompressor()
d.decompress(data)
d.
