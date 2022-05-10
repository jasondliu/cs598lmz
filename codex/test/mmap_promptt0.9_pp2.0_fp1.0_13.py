import mmap
# Test mmap.mmap() giving access to the entire file:
with open('assets/mmap.txt', 'r') as f:
    with open('assets/mmap2.txt', 'w') as fout:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
            text = m.readline()
            print(text)
            fout.write(text)

# Test mmap() giving access to a small section of the file:
with open('assets/mmap.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print(m[0:10])

import tempfile
import os

def show_mapping(m):
    print(f"   length: {m.size}")
    print(f"  readonly: {m.readonly}")
    print(f"      millis: {m.tell()}")
    print(f"  prot flag: {m.prot}")
