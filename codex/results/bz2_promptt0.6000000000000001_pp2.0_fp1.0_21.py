import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as fp:
    decompressor.decompress(fp.read())
# Test BZ2File
with bz2.BZ2File('data/sample.bz2', 'rb') as fp:
    fp.read()
# Test BZ2File with context
with bz2.BZ2File('data/sample.bz2', 'rb') as fp:
    for line in fp:
        print(line)

# Test BZ2File with context and read
with bz2.BZ2File('data/sample.bz2', 'rb') as fp:
    fp.read()
# Test BZ2File with context and readline
with bz2.BZ2File('data/sample.bz2', 'rb') as fp:
    fp.readline()
# Test BZ2File with context and readlines
with bz2.BZ2File('data/sample.
