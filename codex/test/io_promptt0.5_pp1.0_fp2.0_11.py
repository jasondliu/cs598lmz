import io
# Test io.RawIOBase
#
# This test checks that the io.RawIOBase() interface, which is used by
# io.FileIO, is implemented correctly.

import io
import os
import unittest
import tempfile
import struct
import sys
import pickle
import warnings
import errno

