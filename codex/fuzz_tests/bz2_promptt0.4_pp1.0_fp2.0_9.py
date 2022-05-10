import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print('Output is {} bytes'.format(len(result)))
print(result)

# Test BZ2File
bz_file = bz2.BZ2File('bz2_compressed.txt.bz2')
print(bz_file.read())

# Test compress()
uncompressed = b'This is the original text.'
compressed = bz2.compress(uncompressed)
print('Is the compressed file smaller than the original? {}'.format(len(uncompressed) > len(compressed)))
print
