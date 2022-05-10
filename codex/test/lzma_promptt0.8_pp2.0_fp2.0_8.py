import lzma
# Test LZMADecompressor
try:
    import lzma
except ImportError:
    lzma = None

import gzip
import io
import os
import random
import shutil
import stat
import struct
import sys
import tempfile
import time
import zipfile

from test import test_support

# A very large file.
SIZE = 10 * 1024 * 1024

def make_file(name, size=SIZE):
    with open(name, "wb") as f:
        f.write(b"1" * size)

def make_100_files(sizes=[SIZE] * 100):
    for x in range(100):
        make_file(str(x), random.choice(sizes))

