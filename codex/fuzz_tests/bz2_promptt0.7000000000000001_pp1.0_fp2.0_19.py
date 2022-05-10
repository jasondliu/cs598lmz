import bz2
# Test BZ2Decompressor
source = bz2.BZ2File('test.txt.bz2')
target = open('test.txt', 'wb')
decompressor = bz2.BZ2Decompressor()
for data in iter(lambda: source.read(100 * 1024), b''):
	target.write(decompressor.decompress(data))
target.close()
source.close()
# Test BZ2Compressor
source = open('test.txt', 'rb')
target = bz2.BZ2File('test.txt.bz2', 'w')
compressor = bz2.BZ2Compressor()
for data in iter(lambda: source.read(1024), b''):
	target.write(compressor.compress(data))
target.write(compressor.flush())
target.close()
source.close()
