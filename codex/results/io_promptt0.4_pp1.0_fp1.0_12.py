import io
# Test io.RawIOBase
import _io
# Test _io.IOBase

import unittest
import weakref
import gc
import os
import sys
import errno
import time
import tempfile

from test import support

# Test the ability to override the builtin file() type
import builtins

# Test the ability to override the open() builtin
import __builtin__

# Test the ability to override the open() function in the os module
import os

# Test the ability to override the open() function in the io module
import io

# Test the ability to override the open() function in the _io module
import _io

# Test the ability to override the open() function in the posix module
import posix

# Test the ability to override the open() function in the nt module
import nt

# Test the ability to override the open() function in the mac module
import mac

# Test the ability to override the open() function in the os2 module
import os2

# Test the ability to override the open() function in the ce module
import ce

# Test the ability to override the
