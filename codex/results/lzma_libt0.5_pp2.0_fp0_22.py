import lzma
lzma.LZMAFile

# TODO: Remove this hack once we have a proper solution to the
#       "import lzma" problem.
lzma_is_available = True

import os
import shutil
import sys
import tempfile
import zipfile

import numpy as np

# TODO: Remove this hack once we have a proper solution to the
#       "import lzma" problem.
if lzma_is_available:
    import lzma
else:
    import backports.lzma as lzma

import pytest

from pyctest.ctest import CTest
from pyctest.utils import (
    _clean_dir,
    _clean_file,
    _create_dir,
    _create_file,
    _get_file_size,
    _get_random_string,
    _get_random_string_list,
    _get_random_uint,
    _get_random_uint_list,
    _get_random_uint_list_list,
    _get_random_uint_
