import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
d.decompress(data)
# Test BZ2File
compressed = StringIO()
compressed.name = 'fakefile.txt.bz2'
f = bz2.BZ2File(compressed, 'wb')
f.write(data)
f.close()
compressed.seek(0)
bz2.BZ2File(compressed).read()
# Test BZ2File.readline
compressed.seek(0)
bz2.BZ2File(compressed).read(10)
bz2.BZ2File(compressed).readline()
bz2.BZ2File(compressed).readline(10)
bz2.BZ2File(compressed).readline(50)
bz2.BZ2File(compressed).readline()
bz2.BZ2File(compressed).readline()
compressed.close()
