import bz2
# Test BZ2Decompressor
data = open('lorem.txt', 'rb').read()
for i in xrange(1,10,2):
    compressor = bz2.BZ2Compressor(i)
    compressed = compressor.compress(data)
    compressed += compressor.flush()

    decompressor = bz2.BZ2Decompressor()
    output = decompressor.decompress(compressed)
    print len(output)

# Test BZ2Decompress
decompressor = bz2.BZ2Decompressor()
f = open('lorem.bz2', 'rb')
try:
    decompressor.decompress(f.read())
    print "OK"
except EOFError as err:
    print "EOF:", err
