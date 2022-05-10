import mmap
# Test mmap.mmap()
filename = "home/luke/Desktop/test.txt"
#map = mmap.mmap(open(filename).fileno(), 0, mmap.MMAP_PRIVATE, mmap.MAP_SHARED)
map = mmap.mmap(open(filename).fileno(), 0)
index = map.find("\n")
end  = map.rfind("\n")
print(index)
print(end)
print(map[index:end])
map.close()
