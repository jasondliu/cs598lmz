import bz2
# Test BZ2Decompressor

decomp = bz2.BZ2Decompressor()
decomp.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Test BZ2File
bz2.BZ2File('small.bz2').read()

# Test decompression bomb protection.
