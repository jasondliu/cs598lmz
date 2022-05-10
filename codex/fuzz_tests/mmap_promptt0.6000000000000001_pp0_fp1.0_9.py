import mmap
# Test mmap.mmap()
# m = mmap.mmap(-1, 1024)
# m.write(b'Hello')
# m.seek(0)
# m.read(5)
# m.close()
# test mmap.mmap() with tagname
# m = mmap.mmap(-1, 1024, tagname=b'MEM')
# m[:5] = b'Hello'
# m.seek(0)
# m.read(5)
# m.close()
# test mmap.mmap() with fileno
# f = open('/dev/zero')
# m = mmap.mmap(f.fileno(), 1024)
# m.write(b'Hello')
# m.seek(0)
# m.read(5)
# m.close()
# test mmap.mmap() with file
# f = open('/dev/zero')
# m = mmap.mmap(f, 1024)
# m.write(b'Hello')
# m.seek(0)
# m.read(5)
# m.close()
