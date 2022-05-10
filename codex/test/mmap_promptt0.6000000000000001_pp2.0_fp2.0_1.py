import mmap
# Test mmap.mmap.readline()

import os
import mmap
import StringIO

try:
    import fcntl
except ImportError:
    fcntl = None

def main():
    # Open a file and memory-map it.
    fd = os.open('mmap_readline_file', os.O_CREAT | os.O_RDWR)
