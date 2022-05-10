import mmap
# Test mmap.mmap.__doc__

from test import test_support
import unittest
import os
import sys
import stat

# Skip this test if the OS doesn't support mmap
if not hasattr(os, 'MAP_PRIVATE'):
    raise unittest.SkipTest("os.MAP_PRIVATE not defined")

# Skip this test if the OS doesn't support mmap with file descriptors
if not hasattr(mmap, 'mmap'):
    raise unittest.SkipTest("mmap.mmap not defined")

# Skip this test if the OS doesn't support PROT_EXEC
if not hasattr(mmap, 'PROT_EXEC'):
    raise unittest.SkipTest("mmap.PROT_EXEC not defined")

# Skip this test if the OS doesn't support PROT_WRITE
if not hasattr(mmap, 'PROT_WRITE'):
    raise unittest.SkipTest("mmap.PROT_WRITE not defined")

# Skip this test if the OS doesn't support MAP_ANONYMOUS
if not
