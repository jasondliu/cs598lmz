import mmap
# Test mmap.mmap'zero_copy' attribute.

# The 'n' format character is not supported under Windows
# unless a special pyd is loaded.  Ignore this test in that case.

import sys
if sys.platform == 'win32' and not hasattr(sys, 'gettotalrefcount'):
    raise TestSkipped, 'need special pyd for this test on Windows'

m = mmap.mmap(-1, 1)
try:
    print m.zero_copy
except AttributeError:
    print "mmap.mmap object has no attribute 'zero_copy'"
m.close()
