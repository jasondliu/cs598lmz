import lzma
# Test LZMADecompressor

# Test decompression of a small file with a known contents

# Test the decompression of a small file with a known contents.
# The file is compressed with the xz command-line tool, and the
# decompressed output is compared with the original.

# The file is taken from the xz test suite.

# The xz command-line tool is not included in the Python standard
# library. It can be downloaded from http://tukaani.org/xz/

import os
import subprocess
import unittest
import io
import sys

from test import support
from test.support import TESTFN, run_unittest

# The file is taken from the xz test suite.
# http://tukaani.org/xz/xz-5.0.0-test-data.tar.bz2
# The file is compressed with the xz command-line tool.
# The command-line tool is not included in the Python standard library.
# It can be downloaded from http://tukaani.org/xz/

# Compress the file with the xz command-line
