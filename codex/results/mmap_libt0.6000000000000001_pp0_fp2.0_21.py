import mmap
import struct
import sys
import timeit

import numpy as np

if len(sys.argv) != 4:
    print("Usage: " + sys.argv[0] + " <n_rows> <n_cols> <n_trials>")
    sys.exit(1)

n_rows = int(sys.argv[1])
n_cols = int(sys.argv[2])
n_trials = int(sys.argv[3])

n_bytes = n_rows * n_cols * 4

# Create a file to serve as the shared memory.
f = open("/dev/shm/shm", "w+")
f.seek(n_bytes - 1)
f.write(b"\0")
f.close()

# Map the shared memory into our address space.
f = open("/dev/shm/shm", "r+")
buf = mmap.mmap(f.fileno(), n_bytes, mmap.MAP_SHARED, mmap.PROT_WR
