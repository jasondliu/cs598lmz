import mmap
# Test mmap.mmap
map = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)
map[0:1] = b'a'
print(map[0:1])
assert(map[0:1] == b'a')

map[0:1] = b'b'
print(map[0:1])
assert(map[0:1] == b'b')

map[0:1] = b'c'
print(map[0:1])
assert(map[0:1] == b'c')

map[0:1] = b'd'
print(map[0:1])
assert(map[0:1] == b'd')

map[0:1] = b'e'
print(map[0:1])
assert(map[0:1] == b'e')

map[0:1] = b'f'
print(map[0:1])
assert(map[0:1] == b'f')
map.close()
