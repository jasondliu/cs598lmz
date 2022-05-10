import mmap
import os
import shutil
import tempfile
import unittest

from six import wraps


class TestBase(unittest.TestCase):
    """Base class for FileHandler tests."""

    def setUp(self):
        """Creates a temporary directory and a file to log to."""
        self.tempdir = tempfile.mkdtemp()
        self.logfile = os.path.join(self.tempdir, 'test.log')
        self.handler = logging.FileHandler(self.logfile)

    def tearDown(self):
        """Cleans up the temporary directory."""
        shutil.rmtree(self.tempdir)

    def _WaitForFile(self):
        """Waits for the file to be flushed to disk."""
        # When using Python, there is no way to wait for the contents
        # of the file to be flushed to the filesystem.  We can only
        # wait for the file descriptor to be flushed.  So we will
        # sleep for a short moment.  This is needed to prevent
        # occasional test failures due to overly eager
