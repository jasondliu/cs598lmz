import bz2
# Test BZ2Decompressor
data = open('lorem.txt', 'rb').read()
for i in range(1,10):
    print '%d %d bytes' % (i, len(bz2.BZ2Compressor(i).compress(data)))

print 'Self test: ', bz2.decompress(bz2.compress(data)) == data

# Test BZ2File
f = bz2.BZ2File('lorem.txt.bz2', 'wb')
f.write(data)
f.close()

f = bz2.BZ2File('lorem.txt.bz2', 'rb')
print 'File: ', data == f.read()

# Test compress/decompress
print 'Compress: ', bz2.decompress(bz2.compress(data)) == data



# Output:
# 1 513 bytes
# 2 481 bytes
# 3 473 bytes
# 4 469 bytes
# 5 467 bytes
# 6 466 bytes
# 7 466 bytes
# 8 466 bytes

