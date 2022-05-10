import mmap
# Test mmap.mmap() with various combinations of optional arguments.
# The test file is small enough to fit in the default mmap buffer.
#
# Note that if the test fails with a traceback or SystemError, it is
# very likely that your Python failed to allocate the memory area
# requested by mmap.
#
# For example, to test a 256MB allocation on a system with 2GB of
# physical RAM, you may need to give the Python executable up to 3GB
# of address space.  Some systems allow this via a command line option
# (e.g. Linux: python -m mmap_largefile -Xmx3072m).  On other systems
# (e.g. FreeBSD, Mac OS X), you'll need to configure and build a custom
# Python executable.
#
# Written by:  Brett Cannon <brett@python.org>
# Modified for unittest: Trent Mick <TrentM@ActiveState.com>
# Modified for mmap_large: Skip Montanaro <skip@pobox.com>

import os
import random
import sys
import unittest
import mmap


#
