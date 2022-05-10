import io
# Test io.RawIOBase.readinto()
# written by Mike C. Fletcher
# inspired by readinto() test in Lib/test/test_mmap.py

import unittest, os, mmap, io, tempfile, sys, stat

