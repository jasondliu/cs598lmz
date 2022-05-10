import mmap
# Test mmap.mmap()
#
# Note: If the file does not exist, it will be created.
#
# Note: If the file does not fit in real memory, pages will be swapped out
#       to virtual memory.
#
# Note: If the file is larger than real memory, the extra will not be loaded.
#       When you try to access those pages, they will be loaded.
#       mmap is normally used to access files that fit into real memory.
#
# Note: If you try to write to a page that hasn't been loaded, it will be
#       loaded and then written.
#
# Note: If you try to read from a page that hasn't been loaded, you will get
#       zeros.
#
# Note: When you close the mmap, changes are written to the file.
#
# Note: If you want to save memory and don't need to load the entire file into
#       memory, use mmap.ACCESS_COPY.
#       Don't use mmap.ACCESS_READ. It will cause segfaults.
#
# Note: If you don't need to modify
