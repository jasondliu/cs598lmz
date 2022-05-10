import select
# Test select.select on devices which do not allow it.
# On Windows, select.select fails on win32 console handles with
# errno 22 (Invalid Argument).
# On Mac OS X Tiger, select.select fails on tty devices with
# errno 0.

import sys
import os
import select
import errno
try:
    import fcntl
except ImportError:
    pass

if hasattr(select, 'poll'):

    def poll():
        pass

