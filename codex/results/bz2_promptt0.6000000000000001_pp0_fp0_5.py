import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print('Output is {} bytes'.format(len(result)))
print(result)

print('Decompressor has {} unused input bytes'.format(len(decompressor.unused_data)))

compressor = bz2.BZ2Compressor(9)
result = compressor.compress(b'The same line, over and over.\n')
result += compressor.compress(b'The same line, over and over.\n')
result += compressor.flush()
print(result)
# bz2.BZ2Compressor.comp
