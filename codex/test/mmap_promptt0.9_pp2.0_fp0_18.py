import mmap
# Test mmap.mmap()
# - create 4GiB sparse file
# - mmap() with MAP_POPULATE, read/write all pages with
#   random offsets and comparing memory contents
