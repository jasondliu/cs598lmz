import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is %d bytes' % len(data))

decompressor = bz2.BZ2Decompressor()
print('Decompressor is %s bytes' % decompressor.decompress(data))

print('Total decompressed size is %d' % len(decompressor.decompress(data)))
print('Compress ratio is %f' % (len(data) / len(decompressor.decompress(data))))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(b'This is an example')
compressed_data += compressor.flush()
print('Compressed is %d bytes' % len(compressed
