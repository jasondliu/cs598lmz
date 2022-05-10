import mmap
# Test mmap.mmap()
# Test mmap.shmem()
# Test mmap.error exception
# Test Unix mmap flags
# Test mapping large buffers (2GB and beyond, 64-bit machines only)
# Test that we support accessing mappings past the 2GB barrier
# Test msync()
# Test validations on fileno(), filename, access, offset, and length
# File mapping methods
# Test support for MAP_ANON (Unix/Mac) or JFILE_MAP_ANON (Windows)
# Test mprotect()
# Test flush method (macOS, Windows)
# Buffer protocol support
# Test seek, tell and readinto methods
# Test creation of file-backed mappings
# Test resizing mappings
# Test move and copy within a mapping
# Test that small mappings work with an unaligned offset
# Test that mappings are correctly inherited across exec
# Test resizability of mappings

import sys, os, tempfile, unittest
from test.support import (TESTFN, run_unittest, import_module, cpython_only,
                          cpython_only, is_jython)
import
