import mmap
import os
import re
import sys
import tempfile

PY3 = sys.version_info[0] == 3

if PY3:
    from io import StringIO
else:
    from StringIO import StringIO

try:
    import unittest2 as unittest
except ImportError:
    import unittest

