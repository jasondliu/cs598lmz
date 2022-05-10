import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# Verify that we don't segfault when the file object is destroyed.

# The test is not run if the version of Python is too old.
import sys
if sys.version_info[:2] < (2, 6):
    raise SystemExit("This test requires Python 2.6 or later")

# The test is not run if the platform is Windows.
import os
if os.name == 'nt':
    raise SystemExit("This test is not run on Windows")

# The test is not run if the platform is AIX.
import platform
if platform.system() == 'AIX':
    raise SystemExit("This test is not run on AIX")

# The test is not run if the platform is HP-UX.
if platform.system() == 'HP-UX':
    raise SystemExit("This test is not run on HP-UX")

# The test is not run if the platform is IRIX.
if platform.system() == 'IRIX64':
    raise SystemExit("This test is not run on IRIX")

# The test is not run if the platform
