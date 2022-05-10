import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# Issue #11459: check that io.open() accepts a unicode filename
# on Windows.
support.import_module('nt')

# Issue #11459: check that io.open() accepts a bytes filename
# on Windows.
support.import_module('os2')

# Issue #11459: check that io.open() accepts a unicode filename
# on Mac OS X.
support.import_module('macostools')

# Issue #11459: check that io.open() accepts a unicode filename
# on Unix.
support.import_module('posix')

# Issue #11459: check that io.open() accepts a bytes filename
# on Unix.
support.import_module('fcntl')

# Issue #11459: check that io.open() accepts a bytes filename
# on Unix.
support.import_module('resource')

# Issue #11459: check that io.open() accepts a bytes
