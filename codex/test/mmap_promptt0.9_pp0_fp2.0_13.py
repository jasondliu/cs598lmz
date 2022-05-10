import mmap
# Test mmap.mmap
# Note that f.tell() doesn't work correctly.
f = open('mindmaps.html', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
bytesread = m.read(200)
m.seek(10)
bytesread += m.read(200)
m.close()
f.close()
