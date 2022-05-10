import mmap
# Test mmap.mmap(), the constructor.
a = mmap.mmap(-1, 0)
a.name
a.size
a.tagname
a.filename
a.close()

a = mmap.mmap(-1, 0, tagname=os.urandom(11).encode('ascii'))
a.name
a.size
a.tagname == a.name
a.filename
a.close()

# second fileno() with the same filename is omitted.
a = mmap.mmap(0, 1024)
a.name
a.size
a.tagname
a.filename
a.close()

# second fileno() with the same filename is omitted.
a = mmap.mmap(0, 1024, tagname=os.urandom(11).encode('ascii'))
a.name
a.size
a.tagname == a.name
a.filename
a.close()

# When the tagname is not specified in constructor, the filename is used.
a = mmap.mmap('/usr/share/dict/words')
