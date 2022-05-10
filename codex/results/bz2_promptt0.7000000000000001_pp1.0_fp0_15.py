import bz2
# Test BZ2Decompressor
data = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print 'Input is %d bytes' % len(data)
compressor = bz2.BZ2Compressor()
uncompressor = bz2.BZ2Decompressor()
compressed = compressor.compress(data) + compressor.flush()
print 'Compressed is %d bytes' % len(compressed)
uncompressed = uncompressor.decompress(compressed)
print 'Uncompressed is %d bytes' % len(uncompressed)
print 'Uncompressed matches original:', data == uncompressed
# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
uncompressor = bz2.BZ2Decompressor()
compressed = compressor.compress(data) +
