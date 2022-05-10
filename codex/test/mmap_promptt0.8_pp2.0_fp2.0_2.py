import mmap
# Test mmap.mmap
import contextlib
@contextlib.contextmanager
def mmap_ctx(fname):
    with open(fname,"r+b") as f:
        mm=mmap.mmap(f.fileno(),0)
        yield mm
        mm.close()
        
with mmap_ctx("test_mmap.txt") as mm:
    mm[:10]=b'cat'
    
### mmap.mmap(fileno, length, access=ACCESS_READ, offset=0)
### acces=ACCESS_WRITE
# Offsets in a memory map can be treated as integers or as slices.
with mmap_ctx("test_mmap.txt") as mm:
    mm.seek(15)
    print(mm.read(1))
    
# __sizeof__
import sys
print(sys.getsizeof(mm))

# mmap.ACCESS_COPY mmap.ACCESS_READ mmap.ACCESS_WRITE
import os
