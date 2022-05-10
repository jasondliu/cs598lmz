import mmap
# Test mmap.mmap
mmap_obj = mmap.mmap(-1, 13)
print(mmap_obj)

from mmap import *
assert mmap is mmap
from mmap_test import *
f = open(TESTFN, 'wb+')
f.write(b'\0' * mmap.PAGESIZE)
f.flush()
m = mmap(f.fileno(), 0)
print(m)

class MmapWrapper(object):
    def __init__(self, name, flags='r'):
        self._mapping = mmap(name, 0, flags=flags)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._mapping.close()

    def __len__(self):
        return len(self._mapping)

    def __iter__(self):
        return iter(self._mapping)

    def __getitem__(self, key):
        return self._mapping[key]

import sys
