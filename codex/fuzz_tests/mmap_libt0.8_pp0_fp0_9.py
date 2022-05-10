import mmap
import re
import sys


# Build-in Python modules
import os
import shutil
import tempfile
import unittest
import uuid

# Relevant for Python 2/3 compatibility
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import sys_platform

# Make sure Python can find the C++ extension
sys.path.append(os.getcwd())

# Import the extension
import read_model

# Import custom Python modules
import batch_factory
import configuration
import profile_factory
import stub_extension

# Import the Python module containing the test batch file
import batches_shared

class TestProfiles(unittest.TestCase):

    def setUp(self):
        # Remove the temporary directory, if it exists
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

        # Create the temporary directory
        os.mkdir(self.temp_dir)

        # Create the test model
        self.model_id = str
