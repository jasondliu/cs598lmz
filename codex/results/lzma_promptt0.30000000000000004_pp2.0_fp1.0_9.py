import lzma
# Test LZMADecompressor

# This test is a bit awkward to run because it requires a file
# containing random data.  The file test/random_data.lzma was
# created by running the following command:
#
#     dd if=/dev/urandom of=test/random_data.lzma bs=1M count=10
#
# The file is not included in the distribution because it's not
# free software.

# The file test/random_data.lzma is compressed with the
# "extreme" preset, which is not supported by the LZMADecompressor
# class.  The file test/random_data_fast.lzma is compressed with
# the "fast" preset, which is supported.

# The file test/random_data_fast.lzma was created by running the
# following command:
#
#     lzma -z -T0 -9 -e test/random_data
#
# The file is not included in the distribution because it's not
# free software.

import os
import unittest

from test import support

class LZ
