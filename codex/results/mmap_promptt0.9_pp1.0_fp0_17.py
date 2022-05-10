import mmap
# Test mmap.mmap.close_fd  related error.

with open('test.txt', 'wt', closefd=False) as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write('\0')
    m.close()
    f.close()
