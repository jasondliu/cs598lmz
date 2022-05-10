import io
# Test io.RawIOBase.
db = open('file.bz2','rb')
dbfile = bz2.BZ2File(db)
print(type(dbfile.readline()))
# Test io.BufferedIOBase.
db = open('file.bz2','rb')
dbfile = bz2.BZ2File(db)
print(type(dbfile.readline()))
# Test io.TextIOBase.
db = open('file.bz2','rb')
dbfile = bz2.BZ2File(db)
print(type(dbfile.readline()))
# Test io.TextIOBase.
db = open('file.bz2','rb')
dbfile = bz2.BZ2File(db)
print(type(dbfile.readline()))
# Test io.TextIOBase.
db = open('file.bz2','rb')
dbfile = bz2.BZ2File(db)
print(type(dbfile.readline()))
# Test io.TextIOBase.
db = open('file.b
