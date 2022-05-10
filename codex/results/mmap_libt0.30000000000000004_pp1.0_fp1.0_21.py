import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

from distutils.version import LooseVersion

from . import test_utils
from .test_utils import (
    TEST_DIR,
    TEST_DATA_DIR,
    TEST_DATA_FILE,
    TEST_DATA_FILE_SZ,
    TEST_DATA_FILE_SHA1,
    TEST_DATA_FILE_SHA256,
    TEST_DATA_FILE_SHA512,
    TEST_DATA_FILE_MD5,
    TEST_DATA_FILE_CRC32,
    TEST_DATA_FILE_CRC64,
    TEST_DATA_FILE_BLAKE2B,
    TEST_DATA_FILE_BLAKE2S,
    TEST_DATA_FILE_SHA3_224,
    TEST_DATA_FILE_SHA3_256,
    TEST_DATA_FILE_SHA3_384,
    TEST_DATA_FILE_SHA3_512,
    TEST_DATA_FILE_SHAKE128,
    TEST_DATA_
