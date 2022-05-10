import mmap
import tempfile
import unittest

from cStringIO import StringIO
from cStringIO import InputType, OutputType
from cStringIO import StringO, StringI
from cStringIO import _test_mixin
from test import test_support


class StrIOTest(unittest.TestCase, _test_mixin.TestMixinStr):
    io_type = InputType

    def _io_tester(self, s=None, bufsize=-1):
        self.assertIsInstance(s, self.io_type)
        self.check_pos(s)
        self.check_many_reads(s)
        self.check_writes(s)
        self.check_writelines(s)
        self.check_tell(s)
        self.check_seek(s, bufsize)
        self.check_truncate(s)
        self.check_writelines_userlist(s)
        self.check_writelines_error(s)

    def test_basic(self):
        s = self.io_type()
       
