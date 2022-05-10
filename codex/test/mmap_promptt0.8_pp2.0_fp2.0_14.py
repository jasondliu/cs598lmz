import mmap
# Test mmap.mmap object.

def main():
    size = mmap.PAGESIZE
    m = mmap.mmap(-1, size)
    m[0] = b'a'
    m.close()

