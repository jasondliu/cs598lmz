import codecs
codecs.encode('%s\n' % zlib.crc32(u'hello'.encode('utf-8')))

# Now we can check the crc32 of a
# given file and compare it
# to the crc32 of the file in
# the index.

# We can also hash the file,
# and compare that
# instead of the crc32.

# If the file is a directory
# we should do an recursive
# crc32 on all the files
# within the directory.

# If we get a match,
# then we can compare the
# list of files within
# each directory.

# If the list of files
# is the same, we can have
# every file in the directory
# recursively check their
# hashes.

# If the hashes match, then
# we can assume that we've
# found a duplicate

import hashlib
import os
import sys
import zlib

def get_crc32(path):
    """
    >>> test_crc32_file = 'test_crc32.txt'
   
