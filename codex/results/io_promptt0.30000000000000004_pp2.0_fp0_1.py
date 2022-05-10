import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import stat
import time
import random
import shutil
import weakref
import warnings
import contextlib
import functools
import pickle
import gc

from test import support
from test.support import TESTFN, unlink, run_with_locale, check_warnings

# We need to use a unicode filename for the test, but NamedTemporaryFile
# doesn't support that (yet).
def _named_temporary_file(mode='w+b', bufsize=-1, suffix="",
                          prefix=support.TESTFN, dir=None, delete=True):
    """Create a temporary file with a unique name.

    Arguments: 'prefix', 'suffix', 'dir' and 'delete' are the same as for
    mkstemp.
    The file is created as mkstemp() would do it.

    Returns an object with a file-like interface.  The file has no
    name, and will cease to exist when it is closed.
    """
    with
