import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
data = d.decompress(data)

# Test BZ2File
with bz2.BZ2File(filename) as f:
    data = f.read()
    f.seek(-10, os.SEEK_END)
    data = f.read()

# Test BZ2Compressor
c = bz2.BZ2Compressor()
data = c.compress(data)
data = c.flush()

# Test open
with bz2.open(filename) as f:
    data = f.read()
    f.seek(-10, os.SEEK_END)
    data = f.read()
    f.seek(0, os.SEEK_SET)
    data = f.read(5)
    f.seek(0, os.SEEK_SET)
    data = f.readline()
    f.seek(0, os.SEEK_SET)
    data = f.readlines()
    f.seek(0, os.SEEK_SET)
