import mmap
# Test mmap.mmap.__new__ ...
# Test mmap.mmap.flush
# Test mmap.mmap.close
# Test mmap.mmap.find
# Test mmap.mmap.rfind
# Test mmap.mmap.read
# Test mmap.mmap.read_byte
# Test mmap.mmap.readline
# Test mmap.mmap.readlines
# Test mmap.mmap.resize
# Test mmap.mmap.seek
# Test mmap.mmap.size
# Test mmap.mmap.tell
# Test mmap.mmap.write
# Test mmap.mmap.write_byte

# ---------------------------------------------------------------------------------

# Read a whole file.
def read_raw(file):
    """
    Read the contents of a file into a string and return it. 'file' must be an
    open file object positioned at the beginning of the file.
    """
    s = ""
    while True:
        t = file.read(1024)
        if len(t) == 0:
            return s
        s = s +
