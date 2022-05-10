import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0)

import os
import unittest

import mmap_docstring as md

from test import test_support


def with_mmap(size, access=mmap.ACCESS_WRITE, offset=0, tagname=None):
    """Create an mmap object and perform some operations on it.

    The 'with' statement is used to ensure the object is closed before
    the test ends.

    The mmap is created from a file descriptor created by os.pipe().
    The file descriptor is created with the close_fds=True so that
    it will be closed when the popen object is garbage collected.

    The mmap created will have size 'size', and will be accessed using
    the specified 'access' mode.
    """
    r,w = os.pipe()
    m = mmap.mmap(r, size, access, offset)
    if tagname:
        m.tagname = tagname
    try:
        yield m
    finally:
        m.close()
        os.
