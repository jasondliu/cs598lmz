import mmap
import os
import sys
import time
import uuid
import contextlib

import pytest

from ansible.module_utils.six.moves import cStringIO as StringIO
from ansible.module_utils.six import BytesIO

from ansible.module_utils._text import to_bytes, to_text

# Python 2.7 does not have mock.mock_open() built-in
try:
    from unittest.mock import mock_open
except ImportError:
    from mock import mock_open


@contextlib.contextmanager
def patch_open(mocker, text=None):
    if text is None:
        text = "this is a test file"

    m = mocker.mock_open(read_data=text)
    mocker.patch("ansible.module_utils.basic.open", m, create=True)
    yield m


class TestOpenFile(object):
    def test_open_file_success(self, mocker):
        with patch_open(mocker) as m:
            f = basic.open
