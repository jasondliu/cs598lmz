import mmap
# Test mmap.mmap() using mmap.MAP_PRIVATE:
#
# Unix: The write-through option is ignored by the kernel.
#
# Win: The contents of a file mapping are guaranteed to match the contents
# of the file at the time the mapping is created.  This means that, for
# example, if the file is extended after the mapping is created, the
# contents of the file would be visible to the process only starting at
# the original file size and not at the current file size.
#
#   API:  CreateFileMapping, ResizeFile, GetFileSize,
#         CreateFile, CloseHandle.
#

#----------------------------------------------------------------------

import unittest
import mmap
import os
import sys

if sys.platform not in ('win32', 'darwin'):
    # Skip these tests on Linux, et al, since MAP_PRIVATE is not
    # valid for use with anonymous mappings.
    raise unittest.SkipTest("MAP_PRIVATE is not valid here.")

