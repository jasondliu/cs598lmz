import io
# Test io.RawIOBase.readinto()
#
# This test is a modified version of the test from the CPython stdlib
# test.test_io.test_rawio, which was modified for use with MicroPython.

import sys
import time

try:
    import uio
    uio_available = True
except ImportError:
    uio_available = False

try:
    import ustruct
except ImportError:
    print("SKIP")
    raise SystemExit

# Test io.RawIOBase.readinto()

# This test is a modified version of the test from the CPython stdlib
# test.test_io.test_rawio, which was modified for use with MicroPython.

import sys
import time

try:
    import uio
    uio_available = True
except ImportError:
    uio_available = False

try:
    import ustruct
except ImportError:
    print("SKIP")
    raise SystemExit

# Test io.RawIOBase.readinto()

