import select
# Test select.select()
#
# This test is not exhaustive.  It is meant to be run manually.
#
# The test is designed to be run in a subprocess, so that it can
# mess with the file descriptors of the parent process.

import os
import sys
import signal
import time
import select
import subprocess
import unittest

class SelectTest(unittest.TestCase):

    def setUp(self):
        self.read_fd, self.write_fd = os.pipe()

    def tearDown(self):
        os.close(self.read_fd)
        os.close(self.write_fd)

