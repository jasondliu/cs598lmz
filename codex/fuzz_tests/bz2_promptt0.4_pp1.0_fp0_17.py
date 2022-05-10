import bz2
# Test BZ2Decompressor

with bz2.BZ2File('sample.bz2', 'rb') as infile:
    with open('sample.txt', 'wb') as outfile:
        for data in iter(lambda : infile.read(100 * 1024), b''):
            outfile.write(data)
 
# Test BZ2Compressor

with open('sample.txt', 'rb') as infile:
    with bz2.BZ2File('sample.bz2', 'wb') as outfile:
        for data in iter(lambda : infile.read(100 * 1024), b''):
            outfile.write(data)
 
# Test BZ2File

with bz2.BZ2File('sample.bz2', 'rb') as infile:
    for line in infile:
        print(line)

with bz2.BZ2File('sample.bz2', 'wb') as outfile:
    outfile.write(b'Hello World!')
 
# Test BZ2Compressor.compress() and BZ2
