import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is intended to be run with a debug build of Python.
# It exercises gc.collect() and the garbage collection mechanism in
# general.  It is expected to be run with the garbage collector enabled
# and with the garbage collector disabled.  It can be run with the
# cyclic garbage collector enabled and disabled.

import gc
import unittest
import weakref
import sys
import os
import subprocess
import time
import re
import io
import contextlib
import platform
import test.support

# Some tests use a lot of memory.
test.support.set_memlimit(512 * 1024 * 1024)

#
# The tests are organized in three groups:
#
# 1. Tests that are run with the cyclic GC enabled and disabled
# 2. Tests that are run with the cyclic GC disabled
# 3. Tests that are run with the cyclic GC enabled
#
# The cyclic GC is enabled by default.  If it is disabled, it can be
# enabled by setting the environment variable PYTHONCYCLEGC to a
# non-empty string. 
