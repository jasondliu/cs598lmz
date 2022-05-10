import mmap
# Test mmap.mmap.mmap.mmap size = 30
m = mmap.mmap(0, 30, "test", mmap.ACCESS_WRITE)
laststr = m.read(10000) # Read a lot more than is really there.
print ("Last string read/written: ", laststr)

# m[4:4] returns an empty string (doesn't raise an IndexError).

# m[4:3] returns an empty string since 4 is greater than the
# current size of the memory mapped object (0).

# m[4:10] returns an empty string since the current size of the object is 0
# and the high index (9) is greater than the size of the object.

m.close() # don't forget to close.

#%_______________________________________________________________________________
import multiprocessing
import time
import random
import string

def worker():
    """thread worker function"""
    t = random.randrange(1,10)
    time.sleep(t)
    print('sleep: ',t)
    return

for _ in range(5):
    p = multiprocess
