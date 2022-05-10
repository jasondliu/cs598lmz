import mmap
# Test mmap.mmap(0, 1024, 'sharedmem')
print("Before")
import os
if os.path.exists("./Shared"):
    #os.remove("./Shared")
    os.unlink("./Shared")

# ShmCreate
fd = os.open("./Shared", os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o777)
#fd = os.open("./Shared", os.O_RDWR | os.O_EXCL | os.O_CREAT)
#fd = os.open("Sharedmem", os.O_CREAT)
print("File Descriptor:", fd)
m = mmap.mmap(fd, 1024, "sharedmem")
#m = mmap.mmap(0, 1024, "sharedmem")
