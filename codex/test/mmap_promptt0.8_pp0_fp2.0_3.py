import mmap
# Test mmap.mmap'zero_copy' attribute.

# The 'n' format character is not supported under Windows
# unless a special pyd is loaded.  Ignore this test in that case.

import sys
