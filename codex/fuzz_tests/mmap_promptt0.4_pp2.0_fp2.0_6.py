import mmap
# Test mmap.mmap(0, 1, "sharedmem", mmap.ACCESS_WRITE)

# import mmap
# # Test mmap.mmap(0, 1, "sharedmem", mmap.ACCESS_WRITE)
# f = open("sharedmem", "w+b")
# f.write(b"\x00"*1)
# f.close()
# f = open("sharedmem", "r+b")
# m = mmap.mmap(f.fileno(), 1, "sharedmem", mmap.ACCESS_WRITE)
# m.seek(0)
# m.write(b"\x01")
# m.seek(0)
# print(m.read(1))
# m.close()
# f.close()

# import mmap
# import os
# import time
# # Test mmap.mmap(0, 1, "sharedmem", mmap.ACCESS_WRITE)
# f = open("sharedmem", "w+b")
# f.write(b"\x00"*1)
# f.close
