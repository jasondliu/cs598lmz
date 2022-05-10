import io
# Test io.RawIOBase and buffer protocol
# Similar to test_cStringIO, but for raw I/O

import _pyio
from test.support import TestFailingIO, import_module
from test.support.script_helper import assert_python_failure, assert_python_ok

from test import support

from io import FileIO as file

from io import BytesIO as _BytesIO
from io import BufferedIOBase
from io import RawIOBase
from io import UnsupportedOperation
import unittest
from unittest import skipUnless
import os
from os import name as osname
from abc import ABCMeta, abstractmethod

from io import (
    BufferedRWPair, BufferedRandom,
    BytesIO, FileIO, BufferedReader,
    BufferedWriter, BufferedWriter, BufferedRWPair,
    IncrementalNewlineDecoder, TextIOWrapper,
    UnsupportedOperation as UO,
    DEFAULT_BUFFER_SIZE, SEEK_CUR, SEEK_END, SEEK_SET)
import io
from _pyio import StringIO


