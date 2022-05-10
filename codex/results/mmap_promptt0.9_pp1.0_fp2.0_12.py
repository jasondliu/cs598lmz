import mmap
# Test mmap.mmap(-1, length, flags=mmap.MAP_PRIVATE | mmap.MAP_ANON)
# for consistency
try:
    M = mmap.mmap(-1, 0, mmap.MAP_PRIVATE | mmap.MAP_ANON)
    M.close()
    M = mmap.mmap(-1, 0, flags=mmap.MAP_PRIVATE | mmap.MAP_ANON)
    M.close()
except ValueError:
    pass
import pickle
import struct
import sys

# Circular imports
submodule_base = 'test_multiprocessing'
submodule_name = 'submodule1'
submodule_attrs = ['submodule_var', 'submodule_func', 'submodule_unpickable',
                   'TestClass', 'TestSubclass', 'TestBaseSubclass',
    'TestBaseSubclassWithoutInit']

submodule_var = None
submodule_unpickable = test.support.Dummy()

class TestClass:

    def __init__(self):
        self.submodule
