gi = (i for i in ())
# Test gi.gi_code

import dis
import io
import sys
from contextlib import redirect_stdout
from test.support import run_unittest, captured_stdout, captured_stderr

from test.test_iterlen import len

codecmp = dis.cmp_opcode

class StrTest(unittest.TestCase):

    def test_printing(self):
        self.assertEqual(repr(compile("x = 1", "?", "exec")),
                         "<code object <module> at 0x7f2b41837290, file \"?\", line 1>")
        self.assertEqual(repr(compile("x = 1", "f", "exec")),
                         "<code object <module> at 0x7f2b41837290, file \"f\", line 1>")
        self.assertEqual(repr(compile("x = 1", "f", "eval")),
                         "<code object <module> at 0x7f2b41837290, file \"f\", line 1>")
        co = compile("x = 1", "f",
