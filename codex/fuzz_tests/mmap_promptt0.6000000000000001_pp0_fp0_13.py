import mmap
# Test mmap.mmap() call
#
# This is a simple test of the mmap.mmap() call.
#
# This test is important because it validates the mmap.mmap() call.
#
# The following tests are performed:
# Create a file of a certain size
# Map the file with mmap.mmap()
# Map the file with mmap.mmap() in read-only mode
# Map the file with mmap.mmap() with access=ACCESS_COPY
# Map the file with mmap.mmap() with access=ACCESS_READ
# Map the file with mmap.mmap() with access=ACCESS_WRITE
# Map the file with mmap.mmap() with access=ACCESS_DEFAULT
# Map the first half of the file with mmap.mmap()
# Map the first 1/4 of the file with mmap.mmap()
# Map the second half of the file with mmap.mmap()
# Map the second 1/4 of the file with mmap.mmap()
# Map the first 1/8 of the file with mmap.mmap
