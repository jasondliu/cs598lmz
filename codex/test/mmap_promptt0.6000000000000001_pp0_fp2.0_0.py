import mmap
# Test mmap.mmap
import os
import re
import subprocess
import sys
import textwrap
import threading
import unittest
import weakref

from test import test_support
from test.test_support import TESTFN, unlink, unload, import_module

# Use a smallish chunk size to exercise the boundary conditions.
CHUNKSIZE = 1000

# Windows has different semantics for write/flush on file-like objects.
# Using a list of strings instead of a string allows us to work around
# this difference.
_writes_pattern = [
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
]

