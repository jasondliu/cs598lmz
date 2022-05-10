import mmap
# Test mmap.mmap() function
#
# This module provides an interface to the Unix memory mapped file I/O
# facility.  It is an extension to Python's file object, i.e. you can use
# mmap objects in most places where file objects are expected.
#
# https://docs.python.org/3/library/mmap.html

# https://docs.python.org/3/library/mmap.html#mmap.mmap
mem_map = mmap.mmap(-1, 13)

# https://docs.python.org/3/library/mmap.html#mmap.write
mem_map.write(b'Hello Python!')

# https://docs.python.org/3/library/mmap.html#mmap.seek
mem_map.seek(0)

# https://docs.python.org/3/library/mmap.html#mmap.read
mem_map.read(13)

# https://docs.python.org/3/library/mmap.html#mmap.close
mem_map.close()

# Test mm
