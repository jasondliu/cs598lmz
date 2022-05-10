import mmap
# Test mmap.mmap

# test_size = 1024 * 1024 * 1024 * 2
test_size = 1024 * 1024 * 1024 * 1  # 1GB

# output_filename = "/data/tmp/test_mmap_2GB.dat"
output_filename = "/data/tmp/test_mmap_1GB.dat"

# Test write
f = open(output_filename, "w+")
f.truncate(test_size)
f.close()

# Test read
f = open(output_filename, "r+")

# mm = mmap.mmap(f.fileno(), test_size, access=mmap.ACCESS_READ)
# MMap will map the whole file into memory, even if you only read some of it.
# mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
# mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_
