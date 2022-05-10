import mmap
# Test mmap.mmap()
shm_file = "shm.bin"
# "r" == read, "w" == write, "b" == binary file, "rw" == read write binary
shm_file = open(shm_file, "r+b")
# 0 = current position, 4096 == length of the file.
shm = mmap.mmap(shm_file.fileno(), 0)
# print(shm)
# <mmap.mmap object at 0x7f45e2a6d358>
# print(mmap.mmap)
# <class 'mmap.mmap'>

# print(shm[:])
# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
