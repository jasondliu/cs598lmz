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
    print mmapped[0:length]
    # Read content via slice notation.
    mmapped[0:length]
    #print len(mmapped)
    #print mmapped[0:10]
    #print mmapped[0:length]
    # Update content using slice notation; note that new content must have same size.
    mmapped[0:length] = b'\x00' * length
    #print len(mmapped
