import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno
import random
import shutil
import stat
import time
import warnings

from test import support
from test.support import TESTFN, unlink, run_unittest, import_module

# Skip these tests if there is no os.sendfile()
sendfile = import_module('sendfile')

# Skip these tests if there is no os.posix_fadvise()
posix_fadvise = import_module('posix_fadvise')

# Skip these tests if there is no os.posix_fallocate()
posix_fallocate = import_module('posix_fallocate')

# Skip these tests if there is no os.ftruncate()
ftruncate = import_module('ftruncate')

# Skip these tests if there is no os.truncate()
truncate = import_module('truncate')

# Skip these tests if there is no os.path.sameopenfile()
sameopenfile = import_
