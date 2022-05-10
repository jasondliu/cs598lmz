import mmap
# Test mmap.mmap()
f = open(r'C:\Users\Leandro\Documents\Python Scripts\Mapas\itajuba_map.osm', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(m.readline())

# Get a single element of the map
m.seek(100)
print(m.readline())

# Get all elements in the map
print(m[:])

# mmap.mmap() objects have a readline() method for sequential access
m.seek(0)
print(m.readline())

# close the mmap
m.close()

# close the file
f.close()


# Test mmap.mmap(-1, ...)
f = open(r'C:\Users\Leandro\Documents\Python Scripts\Mapas\itajuba_map.osm', 'r+')
# memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
