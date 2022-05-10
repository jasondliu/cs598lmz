import mmap
# Test mmap.mmap vs. mmap.mmap_async
# mmap.mmap_async() is the default, it is not possible to use the regular mmap
# on windows.
# The default mmap_async() is slower than the regular mmap() on linux.
# On windows, mmap_async() is much faster than mmap().

import time
import sys
import os
import mmap

if sys.platform.startswith('win'):
    sys.stdout.write("Windows platform detected.\n")
    sys.stdout.write("Testing mmap_async() and mmap() performance.\n")
    sys.stdout.write("mmap_async() should be faster than mmap().\n")
else:
    sys.stdout.write("Non-Windows platform detected.\n")
    sys.stdout.write("Testing mmap() and mmap_async() performance.\n")
    sys.stdout.write("mmap() should be faster than mmap_async().\n")

