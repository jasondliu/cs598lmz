import bz2
# Test BZ2Decompressor
f = open('test.bz2', 'rb')
decompressor = bz2.BZ2Decompressor()
with open('test.txt', 'wb') as outfile:
    for data in iter(lambda : f.read(100 * 1024), b''):
        outfile.write(decompressor.decompress(data))
f.close()
outfile.close()

# Test BZ2File
with bz2.BZ2File('test.bz2', 'rb') as infile:
    with open('test.txt', 'wb') as outfile:
        for data in iter(lambda : infile.read(100 * 1024), b''):
            outfile.write(data)
infile.close()
outfile.close()
</code>

