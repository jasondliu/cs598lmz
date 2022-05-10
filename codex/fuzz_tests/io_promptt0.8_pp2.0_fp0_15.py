import io
# Test io.RawIOBase and io.BufferedIOBase classes.

import io
import os
from test.support import TESTFN, unlink
from test import libregrtest
from typing import IO, Any, List, Optional, Union
from io import RawIOBase, BufferedIOBase


class CIOBase(RawIOBase):
    def readable(self) -> bool:
        return False

    def writable(self) -> bool:
        return True

    def seekable(self) -> bool:
        return False


class CIO(BufferedIOBase, CIOBase):
    pass


class TextIOBase(io.TextIOBase):
    def readable(self) -> bool:
        return False

    def writable(self) -> bool:
        return True

    def seekable(self) -> bool:
        return False


class TextIOWrapper(io.TextIOWrapper, TextIOBase):
    pass


class TestRawIOBase(libregrtest.BaseTestCase):
    def test_closed_attr(self) -> None:
        r = TestRawIO()
       
