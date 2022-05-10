import io
# Test io.RawIOBase.readinto()
import random
import itertools
import string
import os as _os
# Over-ride BytesIO with our own class in order to test readinto on
# non-regular files:
import _pyio as _orig_io
_orig_RawIOBase = _orig_io.BufferedIOBase
_orig_BufferedIOBase = _orig_io.BufferedIOBase
_orig_FileIO = _orig_io.FileIO
# Set to True to see a guide to what the tests are doing.
_DEBUG = False
_DEBUG_VERBOSE = False
# We'll automatically test both read(n) and read() with very small buffers.
_TEST_BUFFER_SIZE = io.DEFAULT_BUFFER_SIZE
_TEST_BUFFER_SIZE2 = _TEST_BUFFER_SIZE // 2
_TEST_BUFFER_SIZE4 = _TEST_BUFFER_SIZE // 4
# Due to various combinations of readinto() with leading read(), we'll
# sometimes read into a source buffer that contains leading data which
# we must ignore.
_LEAD
