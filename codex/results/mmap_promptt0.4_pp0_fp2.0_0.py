import mmap
# Test mmap.mmap(0, 1, mmap.MAP_SHARED, mmap.PROT_READ)

# import os
# import sys
# import time
# import mmap

# # Copy this file to mmap_write_test.py and run it.
# # Then edit this file and save it.
# # The file should be updated "in place" in the running program.

# fd = os.open('mmap_write_test.py', os.O_RDWR)
# buf = mmap.mmap(fd, 0)

# while True:
#     print(buf.readline())
#     time.sleep(1)

# # os.close(fd)


# import os
# import mmap

# # Memory map binary file
# fd = os.open('binary', os.O_RDWR)
# buf = mmap.mmap(fd, 0)

# # Write a byte to the memory mapped file
# buf[0] = '\x01'

# # Close the descriptor
# os.close(fd)


#
