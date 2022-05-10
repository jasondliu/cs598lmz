import mmap
# Test mmap.mmap()
f = open('/tmp/spam', 'r+b')
map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
map[8:16] = 'eggs'
map.close()
f.close()
print open('/tmp/spam', 'rb').read() # Prints 'Hello eggs!'

# Test mmap.mmap() with offset
f = open('/tmp/spam2', 'wb')
f.write('Hello world!')
f.close()

# Open file and memory-map as read-only
f = open('/tmp/spam2', 'rb')
map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print map[:] # Prints 'Hello world!'

# Open file and memory-map as read-only, with offset
f = open('/tmp/spam2', 'rb')
map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ, offset=6
