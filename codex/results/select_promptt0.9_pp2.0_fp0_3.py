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

else:

    def poll():
        for dev in ['/dev/console',
            '/dev/tty',
            '/dev/tty0',
            '/dev/ptmx',
            '/dev/pts/0',
            '/dev/ptc']:
            try:
                p = select.poll()
                if sys.platform == 'win32' and hasattr(sys.stdin, 'fileno'):
                    fileno = sys.stdin.fileno()
                else:
                    fileno = os.open(dev, os.O_RDONLY)
                try:
                    p.register(fileno,
