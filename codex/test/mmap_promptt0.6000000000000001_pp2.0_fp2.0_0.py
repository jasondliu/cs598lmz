import mmap
# Test mmap.mmap
#import mmap
#f = open("file.txt", "r+")
#map = mmap.mmap(f.fileno(), 0)
#map[0] = 'a'
#map.close()
#f.close()

# Test mmap.mmap() and mmap.ACCESS_COPY
import mmap
f = open("file.txt", "r+")
map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
map[0] = 'a'
map.close()
f.close()

# Test mmap.mmap() and mmap.ACCESS_READ
import mmap
f = open("file.txt", "r+")
map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
map[0] = 'a'
map.close()
f.close()

# Test mmap.mmap() and mmap.ACCESS_WRITE
import mmap
