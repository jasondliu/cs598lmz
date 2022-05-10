import mmap
# Test mmap.mmap.resize() method

import mmap, os

# Create a file that will disappear when mmap object is garbage-collected
# and use it as a data store.
filename = "mmap_test"
f = open(filename, "w+")
size = 100
f.write('\x00' * size)
f.flush()

m = mmap.mmap(f.fileno(), size)
m.resize(10)

# The file should have shrunk to 10 bytes
assert os.path.getsize(filename) == 10

# Resizing to the current size should raise ValueError
try:
    m.resize(10)
except ValueError:
    pass
else:
    raise AssertionError

try:
    m.resize(999999)
except ValueError:
    raise AssertionError

m.close()
f.close()
os.unlink(filename)
# Test mmap.mmap.move() method

import mmap, os

# Create a file that will disappear when mmap object is garbage-collected
