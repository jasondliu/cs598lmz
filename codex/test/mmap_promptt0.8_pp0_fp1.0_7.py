import mmap
# Test mmap.mmap

print("Creating a new memory map with mmap.mmap")
m = mmap.mmap(-1, 10000)
print("Entering text in the memory map")
m.write("Hello Python!")
print("Current contents of memory map: {0}".format(m[:]))
print("Closing the memory map")
m.close()

print("Opening for reading")
m = mmap.mmap(-1, 10000, prot=mmap.PROT_READ)
print("Current contents of memory map: {0}".format(m[:]))
print("Closing the memory map")
m.close()

print("Opening for writing")
m = mmap.mmap(-1, 10000, prot=mmap.PROT_WRITE)
print("Current contents of memory map: {0}".format(m[:]))
print("Closing the memory map")
m.close()
print("Reopening for writing")
m = mmap.mmap(-1, 10000)
print("Current contents of memory map: {0}".format(m[:]))
