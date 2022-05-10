import mmap
# Test mmap.mmap.readline()
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import textwrap
import time
import unittest
import warnings
import weakref

from test import support
from test.support import (
    TESTFN, unlink, unload, run_unittest, import_module,
    cpython_only, check_warnings, captured_stdout, captured_stderr,
    run_with_locale, check_syntax_error, check_impl_detail,
    check_no_resource_warning, requires_zlib, requires_bz2, requires_lzma,
    requires_gzip, requires_xz, requires_lz4, requires_brotli,
    requires_lzma_cffi, requires_lzma_cffi_backend,
    requires_lzma_cffi_backend_lzma, requires_lzma_cffi_backend_xz,
    requires_lzma_cffi_backend_lzma
