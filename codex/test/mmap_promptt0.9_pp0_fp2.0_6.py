import mmap
# Test mmap.mmap vs StringIO.StringIO


def mmap_write(text):
    sIO = StringIO.StringIO(text)
    mm = mmap.mmap(sIO.fileno(), 0, access=mmap.ACCESS_WRITE)
    # Assume '\n' bounded lines
    mlines = text.split('\n')
