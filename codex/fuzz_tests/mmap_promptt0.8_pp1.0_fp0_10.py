import mmap
# Test mmap.mmap() use cases

from test import support
import unittest
from io import BytesIO
from os import urandom
from os.path import exists
from tempfile import mkstemp
from array import array

from mmap import error, rw, ACCESS_READ, ACCESS_WRITE, ACCESS_COPY, ALLOCATIONGRANULARITY, mmap as Mmap



# Get the largest supported length
max_len = Mmap(-1, 0).size()
max_len -= max_len % ALLOCATIONGRANULARITY

# Get the max length for a non-file-backed mmap
max_len_nofile = Mmap(-1, 0, "", rw).size()
max_len_nofile -= max_len_nofile % ALLOCATIONGRANULARITY

# Get the current max length for a file-backed mmap
fd, temp_file_name = mkstemp(prefix='mmap_test_')
f = open(temp_file_name, 'w+b')
f.truncate(max_len)

