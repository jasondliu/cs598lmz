import mmap
# Test mmap.mmap()
#
# On Windows and OSX mmap is implemented using a file.  On Linux and SunOS
# mmap.mmap() can map anonymous pages if given an invalid file handle.
# We test both variants.
#
# Memory mapped files are available as mmap objects.
#
# Operations on a memory-mapped file may or may not be buffered, depending on
# the operating system and the options used.  If the operating system uses
# buffer caching for a file, the memory mapping will also be buffered.
# Applications can avoid the overhead of double buffering by avoiding
# the use of stdio and reading or writing directly to the memory mapping.
#
# It is not possible to resize a mapped region like a normal Python string;
# however, the mmap module provides methods for resizing the mapped file,
# and for creating a new map on a portion of an existing map.
import os
import stat
import contextlib
import mmap
import unittest
import sys
import tempfile
import warnings
import io
import random
import gc
try:
    import threading
except ImportError:
   
