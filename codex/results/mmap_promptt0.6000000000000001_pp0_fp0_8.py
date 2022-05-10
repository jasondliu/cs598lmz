import mmap
# Test mmap.mmap(0, 1)
m = mmap.mmap(0, 1)
import time
time.sleep(3600)

# Test mmap.mmap(-1, 1)
m = mmap.mmap(-1, 1)
import time
time.sleep(3600)

# Test mmap.mmap(0, 1, mmap.MAP_SHARED)
m = mmap.mmap(0, 1, mmap.MAP_SHARED)
import time
time.sleep(3600)

# Test mmap.mmap(-1, 1, mmap.MAP_SHARED)
m = mmap.mmap(-1, 1, mmap.MAP_SHARED)
import time
time.sleep(3600)

# Test mmap.mmap(0, 1, mmap.MAP_PRIVATE)
m = mmap.mmap(0, 1, mmap.MAP_PRIVATE)
import time
time.sleep(3600)

# Test mmap.mmap(-1, 1, mmap.MAP_PR
