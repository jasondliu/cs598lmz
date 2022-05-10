import select
# Test select.select with a file descriptor that is not a socket.

import os
import select
import sys
import tempfile
from test.support import run_unittest, verbose

class FileDescriptorTests(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryFile()
        self.tmp.write(b'a')
        self.tmp.seek(0)

    def tearDown(self):
        self.tmp.close()

    def test_select(self):
        fd = self.tmp.fileno()
        self.assertEqual(select.select([fd], [], [], 0), ([fd], [], []))
        self.assertEqual(select.select([], [fd], [], 0), ([], [fd], []))
        self.assertEqual(select.select([], [], [fd], 0), ([], [], [fd]))

def test_main():
    run_unittest(FileDescriptorTests)

if __name__ == '__main__':
    test_
