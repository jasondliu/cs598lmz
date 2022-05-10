import mmap
# Test mmap.mmap

m = mmap.mmap(0, 100, flag=mmap.MAP_DATA_FILE)

try:
    print(m.size())
finally:
    m.close()


# Test mmap.mmap2

m = mmap.mmap2(0, 100, flag=mmap.MAP_DATA_FILE)

try:
    print(m.size())
except TypeError:
    print("TypeError")
