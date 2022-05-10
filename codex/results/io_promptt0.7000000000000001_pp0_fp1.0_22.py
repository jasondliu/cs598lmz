import io
# Test io.RawIOBase for Python 3

import contextlib
import io
import sys

import pytest

from werkzeug.test import create_environ


class TestRawIOBase:

    def test_full_buffered_read(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                return None

        with MyRawIO() as f:
            with pytest.raises(io.BlockingIOError) as exc_info:
                f.read(1)
            assert exc_info.value.characters_written == 0

    def test_non_full_buffered_read(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b'x'
                return 1

        with MyRawIO() as f:
            assert f.read(1) == b'x'

    def test_full_buffered_read1(self):
        class MyRawIO(io.RawIOBase):
            def readinto1(self, b):
                return
