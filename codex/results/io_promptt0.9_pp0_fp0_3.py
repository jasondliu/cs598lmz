import io
# Test io.RawIOBase
import textwrap
import unittest
from unittest import mock
import warnings
from test import support
from test.support.script_helper import assert_python_failure
try:
    import threading
except ImportError:
    threading = None
try:
    import _testcapi
except ImportError:
    _testcapi = None


IO_METHODS = '''\
read readall readinto readline readlines
seek tell
write writelines
'''.split()
IO_METHODS_NO_READLINES = '''\
read readall readinto readline
seek tell
write writelines
'''.split()


class BasicRawIOBaseTest(object):

    def test_constructor(self):


        class A(io.RawIOBase):

            def __init__(self):
                self.myattr = 23

            def readinto(self):
                pass
        a = A()
        self.assertIsInstance(a, io.RawIOBase)
        self.assertEqual(a.myattr, 23)
    io_methods =
