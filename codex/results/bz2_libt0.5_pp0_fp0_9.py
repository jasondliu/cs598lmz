import bz2
bz2.decompress(bz2.compress(data)) == data

f = bz2.BZ2File('file.bz2', 'wb')
f.write(data)
f.close()

f = bz2.BZ2File('file.bz2', 'rb')
f.read() == data

f = bz2.BZ2File('file.bz2', 'rb')
f.close()

f = bz2.BZ2File('file.bz2', 'rb')
f.seek(10)
f.read()

f = bz2.BZ2File('file.bz2', 'rb')
f.seek(10)
f.tell()

f = bz2.BZ2File('file.bz2', 'rb')
f.seek(10)
f.readline()

f = bz2.BZ2File('file.bz2', 'rb')
f.seek(10)
f.readlines()

f = bz2.BZ2
