import mmap
# Test mmap.mmap
map = mmap.mmap(0, 1024, "Testmmap")
map[0] = "a"
print map[0]

map.close()

print "OK"
