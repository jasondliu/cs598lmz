import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(len(data))
bz2_decompress = bz2.BZ2Decompressor()
print(bz2_decompress.decompress(data))
print(bz2_decompress.unconsumed_tail)

# Test BZ2Compressor
original_data = b'This is the original text.'
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(original_data)
print(compressed_data)
final_data = compressor.flush()
print(final_data)
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(compressed_data))
print(dec
