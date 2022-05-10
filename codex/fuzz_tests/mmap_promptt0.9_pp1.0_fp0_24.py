import mmap
# Test mmap.mmap()'s acceptability of the file's mode:

# print(mmap.mmap.__doc__)

# mmap.ACCESS_READ
# Open the file for reading. The file must exist.
# mmap.ACCESS_WRITE
# Open the file for writing. The file must exist.
# mmap.ACCESS_COPY
# Create a private copy-on-write mapping. Changes to the contents of the
# mmap object will be private to this process, and will not be visible to
# other processes mapping the same file. The file must exist.

# 二进制文件变成内存映射文件对象
f=open(r"./tmp/memorymmap.bin","rb+")
# mmap_object = mmap.mmap(f.fileno(), 0)
mmap_object = mmap.mmap(f.fileno(), 0)
# mmap_object = mmap.mmap(f.fileno(), 0,access=mmap.ACCESS_READ
