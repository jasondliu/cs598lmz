import mmap
# Test mmap.mmap()
import os
import shutil
import sys
import tempfile
import textwrap
import time
import struct
import math
import unittest
import weakref
import functools
from test import support
from test.support.script_helper import assert_python_ok


def create_file(path, size):
    """
    Create a file of `size` bytes.
    """
    try:
        with open(path, "w+b") as f:
            f.seek(size-1)
            f.write(b"\x00")
    except EnvironmentError as e:
        if e.errno != errno.ENOSPC:
            raise
        raise unittest.SkipTest("Insufficient space to create the file")


def create_empty_file(path):
    """
    Create an empty file.
    """
    create_file(path, 0)


def check_size(test, path, size):
    """
    Check the size of a file.
    """
