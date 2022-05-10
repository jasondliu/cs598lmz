import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
bz2_decompressor.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

# Test BZ2Compressor
bz2_compressor = bz2.BZ2Compressor()
bz2_compressor.compress(b"hello world")
bz2_compressor.flush()

# Test BZ2File
bz2_file = bz2.BZ2File('file.bz2', 'wb')
bz2_file.write(b"hello world")
bz2_file.close()
bz2_file = bz2.BZ2File('file.bz2', 'rb')
bz2_file.read
