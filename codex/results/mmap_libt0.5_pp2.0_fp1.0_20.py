import mmap
import os
import struct
import sys

#
# Some constants
#

# The following constants are used to determine the format of the
# mmap'ed files.
#
# For more information, see the comments in the header file.

# The magic number to use in the header.
MAGIC = 0x5AA5F00D

# The version number to use in the header.
VERSION = 1

# The maximum number of entries in the index.
MAX_INDEX_ENTRIES = 100

# The maximum size of the index file.
MAX_INDEX_FILE_SIZE = 65536

# The maximum size of a data file.
MAX_DATA_FILE_SIZE = 1048576

# The maximum size of a data file.
MAX_DATA_FILE_SIZE = 1048576

# The maximum size of a data file.
MAX_DATA_FILE_SIZE = 1048576

# The maximum size of a data file.
MAX_DATA_FILE_SIZE = 1048576

# The maximum size of a data file.
MAX_DATA_FILE_SIZE = 10
