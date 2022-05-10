import mmap
import os
import re
import sys
import tempfile
import unittest

import bz2
import gzip
import lzma

import pytest

from . import util

# XXX: If a file is open for writing, we don't want to open it for reading.
# Or, we could close it for writing, open for reading, and then open for
# writing again.  For now, just make sure we don't have a file open for both
# reading and writing.

# Python 2.5's io module doesn't have a BufferedReader or BufferedWriter
# class, so just use the unbuffered versions.
BufferedIOBase = io.BufferedIOBase
BufferedReader = io.BufferedReader
BufferedWriter = io.BufferedWriter
BufferedRWPair = io.BufferedRWPair
BytesIO = io.BytesIO

if sys.version_info >= (3, 3):
    import _pyio as _io
    RawIOBase = _io.RawIOBase
    FileIO = _io.FileIO
else:
    RawIOBase =
