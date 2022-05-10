import io
# Test io.RawIOBase interfaces
import socket
import time
from os import path
from threading import Thread
from unittest.mock import Mock, patch

from parameterized import parameterized

from mps_youtube.utils import (
    FileWrapper, length, MapResponse, NetworkTime, partial, restarized)


def ThreadMock(*args, **kwargs):
    mock = Mock()
    mock.start = Mock()
    return mock


class TestFileWrapper:

    @parameterized.expand([
        (b'foo', 0, 0, b''),
        (b'4711', 0, 2, b'47'),
        (b'4711', 2, 2, b'11'),
        (b'4711', 3, 2, b''),
        (b'4711', 1, -2, b'7'),
        (b'4711', 1, -1, b'71'),
        (b'4711', 0, 0, b''),
    ])
    def test__read(self, full, start, size, exp):
        actual = FileWrapper
