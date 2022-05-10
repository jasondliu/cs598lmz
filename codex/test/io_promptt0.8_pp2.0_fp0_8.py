import io
# Test io.RawIOBase methods

import _thread

try:
    import _testinternalcapi
except ImportError:
    _testinternalcapi = None

try:
    from _testcapi import getargs_eintr
except ImportError:
    getargs_eintr = None

import os
import sys
import unittest
import weakref
