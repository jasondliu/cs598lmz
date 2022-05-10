import mmap
# Test mmap.mmap(0, 1, tagname='foo', access=mmap.ACCESS_READ)
# This should not segfault
# The segment is empty, but still count as a segment
