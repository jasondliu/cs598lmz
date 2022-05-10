import io
# Test io.RawIOBase methods

# The tests are structured as follows:
#
#   * Each test method tests a specific RawIOBase method
#   * The first part of each method is common to all tests and checks that
#     the test can run with the current implementation of the io module
#   * The second part of each method is specific to the tested method
#

import io
import os
import stat
import struct
import sys
import tempfile
import unittest
import warnings

