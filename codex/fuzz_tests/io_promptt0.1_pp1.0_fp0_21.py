import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Issue #7995: if the io module is imported before the _io module,
# io.open() will not be able to call _io.open()
import _io
import io

# Issue #7995: if the _io module is imported before the io module,
# io.open() will not be able to call _io.open()
import io
import _io

# Issue #7995: if the _io module is imported before the io module,
# io.open() will not be able to call _io.open()
import io
import _io

# Issue #7995: if the _io module is imported before the io module,
# io.open() will not be able to call _io.open()
import io
import _io

# Issue #7995: if the _io module is imported before the io module,
# io.open() will not be able to call _io.open()
import io

