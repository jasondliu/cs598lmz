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

import zc.buildout.testing
import zc.buildout.tests

from zc.buildout.tests import easy_install_SetUp

setUp = easy_install_SetUp


def _test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite(
            'README.rst',
            setUp=setUp,
            tearDown=zc.buildout.testing.buildoutTearDown,
            ),
        doctest.DocFileSuite(
            'README.rst',
            setUp=setUp,
            tearDown=zc.buildout.testing.buildoutTearDown,
            optionflags=doctest.ELLIPSIS,
