import io
# Test io.RawIOBase implementations
import unittest
import tempfile
import os
import random
import io
import sys
from io import BytesIO, StringIO, BufferedIOBase
from _io import BufferedWriter, BufferedReader, BufferedRWPair, BufferedRandom
from _pyio import IncrementalNewlineDecoder, TextIOWrapper
import _testbuffer
from test import support
from test.support import run_unittest, cpython_only
from test.support import requires_resource, requires_IEEE_754

def normalize_bytearr_rspaces(ba):
    # Normalize the trailing spaces in a bytearray so that comparison between
    # 32-bit and 64-bit builds gives consistent results.
    # See <https://bugs.python.org/issue12278> for details.
    i = len(ba)
    while i > 0 and ba[i-1] == 32:
        i -= 1
    return ba[:i]

def normalize_charbuf_rspaces(buf):
    return normalize_bytearr_rspaces
