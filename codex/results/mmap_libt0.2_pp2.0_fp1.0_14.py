import mmap
import os
import re
import subprocess
import sys
import tempfile
import time
import unittest

from . import utils

from . import test_base
from . import test_utils

from . import test_base
from . import test_utils

from .test_base import TestBase
from .test_utils import TestUtils

class TestUtils(TestBase):
    """
    Test the utility functions in the utils module.
    """
    def test_get_file_size(self):
        """
        Test the get_file_size function.
        """
        # Create a temporary file.
        fd, path = tempfile.mkstemp()
        os.close(fd)

        # Write some data to the file.
        with open(path, 'w') as f:
            f.write('test')

        # Get the file size.
        size = utils.get_file_size(path)

        # Check the file size.
        self.assertEqual(size, 4)

        # Remove the temporary file.
        os
