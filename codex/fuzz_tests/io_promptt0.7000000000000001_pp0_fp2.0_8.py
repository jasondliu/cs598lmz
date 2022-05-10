import io
# Test io.RawIOBase for absolute-seek support
import os
import platform
import random
import re
import shutil
import stat
import sys
import tempfile
import time
import unittest
import warnings
import weakref

try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

from test import support
from test.support import (TESTFN, TESTFN_UNICODE, unlink, unlink, rmtree,
                          unlink, unlink, HOST, import_module,
                          run_with_locale, requires_zlib, requires_bz2,
                          requires_lzma, requires_gzip, bigmemtest,
                          cpython_only, CODECS, check_warnings,
                          findfile, run_with_tz, strip_python_stderr,
                          requires_resource, _2G, open_urlresource,
                          verbose, make_legacy_pyc,
                          bind_port)

if not hasattr(os, 'SEEK_HO
