import mmap
# Test mmap.mmap with create=False
m = mmap.mmap(0, 100)
m[0]
# Test mmap.mmap with size=0
m = mmap.mmap(0, 0)
m[0]
"""Expected output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot mmap an empty file
"""
# Test mmap.mmap with negative size
m = mmap.mmap(0, -1)
m[0]
"""Expected output:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot mmap an empty file
"""
# Test mmap.mmap with zero-sized file and negative size
m = mmap.mmap(-1, 0, mmap.MAP_SHARED, mmap.PROT_READ|mmap.PROT_WRITE, 0)
m[0]
