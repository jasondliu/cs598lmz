import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings
from test import support
from test.support import import_module

# Skip tests if there is no os.sendfile()
sendfile = import_module('sendfile')

# Skip tests if there is no os.posix_fadvise()
posix_fadvise = import_module('posix_fadvise')

# Skip tests if there is no os.posix_fallocate()
posix_fallocate = import_module('posix_fallocate')

# Skip tests if there is no os.O_TMPFILE
O_TMPFILE = import_module('O_TMPFILE')

# Skip tests if there is no os.O_PATH
O_PATH = import_module('O_PATH')

# Skip tests if there is no os.O_DIRECT
O_DIRECT = import_module('O_DIRECT')

# Skip tests if there is no os.O_NOFOLLOW
O_NOFOLLOW = import_module('O_
