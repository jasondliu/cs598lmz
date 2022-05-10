import mmap
# Test mmap.mmap function.
# Arguments:
#   - filename: string, file name
#   - length: int, length of memory-mapped file
# Return:
#   - mmapped: mmap.mmap object.
def mmap_test(filename, length=1024):
    # Open file in read-write mode.
    fd = os.open(filename, os.O_RDWR)
    # Memory-map the file, size 0 means whole file.
    mmapped = mmap.mmap(fd, length)
    # Read content via standard file methods.
    #print len(mmapped)
    #print mmapped[0:10]
