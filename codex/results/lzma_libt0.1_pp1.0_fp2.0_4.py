import lzma
lzma.LZMAFile

import os
import sys
import time
import shutil
import subprocess
import tempfile
import threading
import traceback

import pytest

from . import util
from . import config
from . import sandboxlib
from . import testlib
from . import vmnetfs_testlib

from .sandboxlib import Sandbox, SandboxError, SandboxTimeoutError
from .testlib import assert_equal, assert_not_equal, assert_raises
from .vmnetfs_testlib import VmnetfsTest, VmnetfsTestError

# -----------------------------------------------------------------------------
# Test cases.

class TestSandbox(VmnetfsTest):
    """Test cases for the Sandbox class."""

    def test_init(self):
        """Test Sandbox.__init__()."""
        with Sandbox(config.build_dir) as s:
            assert_equal(s.cwd, config.build_dir)
            assert_equal(s.timeout, None)
            assert_equal(s.stdin, None)
            assert_equal(
