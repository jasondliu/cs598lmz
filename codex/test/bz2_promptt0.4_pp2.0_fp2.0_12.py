import bz2
# Test BZ2Decompressor

bz_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz_decomp = bz2.BZ2Decompressor()
bz_decomp.decompress(bz_data)

# Test BZ2File

bz2_file = bz2.BZ2File('test.bz2')
bz2_file.read()

# Test BZ2Compressor

bz_comp = bz2.BZ2Compressor()
bz_comp.compress(b'Hello World')
bz_comp.flush()

# Test BZ2File

bz2_file = bz2.BZ2File('test.bz2', 'w')
