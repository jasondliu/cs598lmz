import ctypes
# Test ctypes.CFUNCTYPE.
#
# This test is not appropriate for the Python test suite because it
# requires the ability to make a shared library.  But it is a useful
# test of ctypes and it can be run on any platform that allows
# dynamic loading of shared libraries.

import unittest
import os
import sys
import tempfile
import ctypes
from ctypes import *

# Create a temporary shared library (on Windows this will be a DLL).
#
# The library has a single function that returns the result of adding
# its arguments.

tmpdir = tempfile.gettempdir()

if sys.platform == 'cygwin':
    from distutils.ccompiler import new_compiler
    from distutils.sysconfig import customize_compiler
    from distutils.errors import CompileError, LinkError
    from distutils.core import Extension

    # Compile a shared library (dll) on Cygwin.  This is complicated
    # since Cygwin Python uses MSVC, but it is necessary to test the
    # ctypes module on Cygwin.

    compiler = new_compiler
