import bz2
# Test BZ2Decompressor

comp_data = bz2.compress(b'This is a test')
comp_data

decomp = bz2.BZ2Decompressor()
decomp.decompress(comp_data)

decomp.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
decomp.flush()

# Test BZ2File

bz2.BZ2File(io.BytesIO(comp_data))
bz2.BZ2File(io.BytesIO(comp_data), 'rb')
bz2.BZ2File('test.bz2', 'wb')
bz2.BZ2File('test.bz2', 'wb', compresslevel=9)

with bz2.BZ2File('test.b
