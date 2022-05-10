import mmap
# Test mmap.mmap

# 1. Create a memory-map to an in-memory buffer
# 2. Write a simple array of data
# 3. Read from the memory-map as if it were a file
# 4. Close the memory-map
# 5. Verify that data was read correctly

import mmap
import numpy as np

# Create an in-memory binary file and write some data to it
with open("data.bin", "wb") as f:
    f.write(np.arange(10, dtype=np.float32))

# Open the file for reading
f = open("data.bin", "rb")

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
data = np.frombuffer(m, dtype=np.float32)

# Close the memory-map
m.close()

# Close the file
f.close()

# Verify that the data was read correctly
print(data)

# [0. 1. 2. 3. 4. 5.
