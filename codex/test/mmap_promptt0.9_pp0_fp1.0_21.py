import mmap
# Test mmap.mmap
# https://docs.python.org/2/library/mmap.html

example = mmap.mmap(-1, 1000)
example[:2] = "\xff\xff";
example.seek(0);
