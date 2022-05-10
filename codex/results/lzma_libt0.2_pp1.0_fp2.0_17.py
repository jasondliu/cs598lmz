import lzma
lzma.LZMAError

import os
import sys
import time
import shutil
import tempfile
import unittest
import zipfile

from test import support
from test.support import TESTFN, run_unittest, import_module

# TESTFN is set by test_support.py.
TESTFN2 = TESTFN + "2"
TESTFNDIR = TESTFN + "d"
FIXEDTEST_SIZE = 1000

def _create_testzip():
    with zipfile.ZipFile(TESTFN, "w", zipfile.ZIP_STORED) as zipfp:
        for fpath, fdata in SMALL_TEST_DATA:
            zipfp.writestr(fpath, fdata)

def _create_testzip_with_bad_crc32():
    with zipfile.ZipFile(TESTFN, "w", zipfile.ZIP_STORED) as zipfp:
        for fpath, fdata in SMALL_TEST_DATA:
            zinfo = zipfile.ZipInfo(fpath, time.local
