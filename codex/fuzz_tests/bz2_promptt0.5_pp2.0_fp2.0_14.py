import bz2
# Test BZ2Decompressor object

decompressor = bz2.BZ2Decompressor()

with bz2.open('file.bz2', 'rb') as input:
    with open('file.out', 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))

# Test BZ2File class

with bz2.BZ2File('file.bz2', 'rb') as input:
    with open('file.out', 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(data)
# bz2.BZ2File.readlines()

with bz2.BZ2File('file.bz2', 'rb') as input:
    for line in input:
        print(line)
# bz2.BZ2File.readline()

with bz2.BZ2File('file.bz2', 'rb') as input:

