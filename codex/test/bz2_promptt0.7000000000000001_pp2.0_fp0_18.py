import bz2
# Test BZ2Decompressor
print("BZ2Decompressor :")
bz_comp = bz2.BZ2Compressor()
print(bz_comp.compress(b'hello world!'))
print(bz_comp.flush())

bz_decomp = bz2.BZ2Decompressor()
print(bz_decomp.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
