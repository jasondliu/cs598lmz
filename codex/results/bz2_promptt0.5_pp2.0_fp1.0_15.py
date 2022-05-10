import bz2
# Test BZ2Decompressor
print ('Test BZ2Decompressor:')
decompressor = bz2.BZ2Decompressor()
with open('./tmp/data.bz2', 'rb') as input:
    for block in iter(lambda : input.read(100 * decompressor.decompress(input.read(100))), b''):
        print (block)

# Test BZ2Compressor
print ('Test BZ2Compressor:')
compressor = bz2.BZ2Compressor()
with open('./tmp/data.bz2', 'wb') as output:
    for data in ['Hello', ' ', 'World', '!']:
        output.write(compressor.compress(data))
output.write(compressor.flush())
