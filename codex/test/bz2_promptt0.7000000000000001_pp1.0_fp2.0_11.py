import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('BZ2Decompressor: ', data)

bz2_comp = bz2.BZ2Compressor()
result = bz2_comp.compress(data)
print('Compressed: ', result)
bz2_decomp = bz2.BZ2Decompressor()

try:
    print('Decompressed: ', bz2_decomp.decompress(result))
except IOError as e:
    print('ERROR: ', e)

print('Feed compressor: ', bz2_decomp.decompress(data))
