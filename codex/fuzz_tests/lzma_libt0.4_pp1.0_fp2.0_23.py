import lzma
lzma.LZMAFile
import os
import random
import re
import shutil
import subprocess
import sys
import time
import unittest
import zipfile

from test import support
from test.support import TESTFN, run_unittest, unlink, unload, verbose, \
    import_module, import_fresh_module, check_warnings, requires
from test.support.script_helper import assert_python_ok

# Skip tests if the zlib module does not exist.
zlib = support.import_module('zlib')

# Skip tests if the bz2 module does not exist.
bz2 = support.import_module('bz2')

# Skip tests if the lzma module does not exist.
lzma = support.import_module('lzma')

# Skip tests if the _bz2 module does not exist.
_bz2 = support.import_module('_bz2')

# Skip tests if the _lzma module does not exist.
_lzma = support.import_module('_lzma
