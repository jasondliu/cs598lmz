import bz2
# Test BZ2Decompressor.read() arguments
for bz2file in glob.glob('test.*'):
    print(bz2file)
    with open(bz2file, 'rb') as bzip_file:
        bz2decompressor = bz2.BZ2Decompressor()
        content = bz2decompressor.decompress(bz2decompressor.read())
    print(content)

""
