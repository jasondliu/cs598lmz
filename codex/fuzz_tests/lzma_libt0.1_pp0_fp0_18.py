import lzma
lzma.LZMAError

import os
import sys
import time
import shutil
import subprocess
import tempfile
import unittest

import pytest

from test import support
from test.support import TESTFN, run_unittest, unlink, unload, import_module

# Skip tests if the _lzma module doesn't exist.
lzma = import_module('lzma')

# Skip tests if the _lzma module is too old.
requires_compression = unittest.skipUnless(
    hasattr(lzma, 'LZMACompressor'),
    'requires _lzma.LZMACompressor')
requires_decompression = unittest.skipUnless(
    hasattr(lzma, 'LZMADecompressor'),
    'requires _lzma.LZMADecompressor')
requires_check = unittest.skipUnless(
    hasattr(lzma, 'check'),
    'requires _lzma.check')
requires_format = unittest.skipUnless(
   
