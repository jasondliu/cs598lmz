import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')

from . import lib
from . import util

import logging
log = logging.getLogger(__name__)

# TODO:
#   - add a way to set a flag when the file is modified outside of the library
#     (i.e. by another application)
#   - add a way to get the size of the file
#   - add a way to get the size of the file on disk (i.e. sum of the size of
#     all the extents)

# XXX: add __del__ to unmap the file?

# XXX: need a way to sync the file to disk?

# XXX: inode may be the same for different files (e.g. hardlinks)
#      => need to check that the file is the same one (i.e. same size)

# XXX: add a way to check that the file is not modified outside the library?
#      => maybe check the size of the file and the size of the extents?
#      => maybe add a flag in the file to indicate that the file is modified
#         outside of
