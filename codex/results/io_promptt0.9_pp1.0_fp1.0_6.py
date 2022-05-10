import io
# Test io.RawIOBase with all of the special methods

import io
import unittest

from test.support import (run_unittest, findfile, import_module, TESTFN)

# If subprocess support is available, try to create a subprocess that uses the
# standard I/O file descriptors to write some data.
try:
    import subprocess
except ImportError:
    subprocess = None

try:
    import fcntl
except ImportError:
    fcntl = None


class TestRawIOBase(unittest.TestCase):

    def setUp(self):
        if subprocess:
            with open(TESTFN, "w") as f:
                self.proc = subprocess.Popen(
                    ["python", "-c",
                    'import sys; sys.stdout.write("line1\\nline2\\nline3\\n")'],
                    stdout=f)
                self.proc.wait()
            self.f = open(TESTFN, "rb")
        else:
            self.f = io.BytesIO(b"line
