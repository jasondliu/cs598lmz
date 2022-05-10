import bz2
# Test BZ2Decompressor.read()
decompressor = bz2.BZ2Decompressor()
with bz2.open(path, 'rb') as f:
    decompressor.decompress(f.read(100))
    decompressor.flush()
# Test BZ2File.read()
with bz2.open(path, 'rb') as f:
    f.read(100)
with bz2.open(path, 'rb') as f:
    f.read(100)
 
# BZ2File.readall()
with bz2.open(path, 'rb') as f:
    f.readall()
# Test BZ2File.read()
with bz2.open(path, 'rb') as f:
    f.read(100)
# Test BZ2File.seek()
with bz2.open(path, 'rb') as f:
    f.seek(101)
    f.seek(-102, 2)
    f.seek(101, 1)
    f.seek(4, 1)
    f.seek(0,
