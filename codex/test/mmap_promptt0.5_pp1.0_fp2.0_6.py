import mmap
# Test mmap.mmap
import mmap
import os
import time

f = open("sample.txt", "w+")

# zero fill
f.write(bytes(os.stat("sample.txt").st_size))

f.close()

f = open("sample.txt", "r+b")

# memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)

# read content via standard file methods
print(mm.readline())  # prints "Hello Python!"

# read content via slice notation
print(mm[:5])  # prints "Hello"

# update content using slice notation;
# note that new content must have same size
mm[6:] = b" world!\n"

# ... and read again using standard file methods
mm.seek(0)
print(mm.readline())  # prints "Hello  world!"

# close the map
mm.close()

# close the file
f.close()

# Test mmap.mmap
import mmap
import os
import time

f
