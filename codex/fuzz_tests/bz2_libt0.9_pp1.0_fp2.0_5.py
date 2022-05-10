import bz2
bz2.decompress(bz2.compress(data))

f = bz2.BZ2File('file.bz2', 'w')
f.write(data)
f.close()

f = bz2.BZ2File('file.bz2', 'r')
data = f.read()
f.close()
