import bz2
# Test BZ2Decompressor
bz2.BZ2Decompressor()

# Test BZ2File
bz2.BZ2File('/dev/null')

# Test BZ2Compressor
bz2.BZ2Compressor()

# Test decompress
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Test compress
bz2.compress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Test compress
bz2.comp
