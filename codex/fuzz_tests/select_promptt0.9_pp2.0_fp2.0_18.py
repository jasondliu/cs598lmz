import select
# Test select.select()
import socket
import sys
import unittest

from datetime import datetime as dt
from io import StringIO as stre, BytesIO as byte
from io import TextIOBase
from os import fdopen, O_APPEND, O_CREAT, O_RDONLY, O_RDWR, O_WRONLY
from os import close
from os import stat as os_stat, SEEK_END, SEEK_SET
from os.path import exists, abspath, isdir, curdir, join, dirname

from test import support
from test.support import TESTFN, TESTFN_UNENCODED, run_with_locale
from test.support.script_helper import assert_python_ok, assert_python_failure

# If we ever get a version of Python that supports opendir(), then create a
# version of TESTFN that is guaranteed to be on the same filesystem as the
# current working directory, so that we can test the effects of changing to
# another directory and back.
_CWD_FILESYSTEM = None

# TESTFN is encoded to the
