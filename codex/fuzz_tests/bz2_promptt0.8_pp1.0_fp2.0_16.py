import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xc8N\x18\x00\x00\x00\x01\x00\x00\x00\xff\xff\xff\xff\xff\x01\x00\x00\xff\xff\xff\xff'
bz2.decompress(data)
# Test BZ2Decompressor.decompress
data = open('example.tar.bz2', 'rb').read(500)
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data)
open('example.tar.bz2', 'rb').read(500)
# Test BZ2Decompressor.flush
data = open('example.tar.bz2', 'rb').read()
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data[:500])
decompressor.flush()
decompressor.decompress(data[500:])
# Test BZ2Decompressor.unused_data
data = open
