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
    try:
        os.write(fd, 'Hello\nworld\n')
        m = mmap.mmap(fd, 0)
        if fcntl:
            fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)
        line = m.readline()
        print repr(line)
        line = m.readline()
        print repr(line)
        line = m.readline()
        print repr(line)
        m.close()
    finally:
        os.close(fd)
        os.unlink('mmap_readline_file')

    # Memory-map a string.
    m
