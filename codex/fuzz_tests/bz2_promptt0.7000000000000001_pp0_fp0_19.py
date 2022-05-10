import bz2
# Test BZ2Decompressor by decompressing some data from the Python source.

# BytesIO is used to simulate a file.

src = bz2.BZ2File(sys.argv[1])
dst = open(sys.argv[2], 'wb')

decompressor = bz2.BZ2Decompressor()
for block in iter(lambda : src.read(100 * 1024), b''):
    dst.write(decompressor.decompress(block))

dst.close()
src.close()
