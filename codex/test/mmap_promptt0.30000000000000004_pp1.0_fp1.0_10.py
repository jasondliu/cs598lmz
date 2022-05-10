import mmap
# Test mmap.mmap(0, 1)
# This is a test for SF bug #1531463: mmap.mmap(0, 1) fails on Windows
# with a WindowsError of "Not enough storage is available to process
# this command"
#
# The bug is triggered by the fact that the mmap module uses a zero
# length buffer as a marker for an uninitialized buffer.  The Windows
# kernel doesn't like zero length mappings.  The fix is to use a
# length of 1 instead.

import mmap

m = mmap.mmap(0, 1)
m.close()
