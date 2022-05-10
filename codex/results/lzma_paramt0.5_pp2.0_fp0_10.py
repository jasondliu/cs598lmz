from lzma import LZMADecompressor
LZMADecompressor()

# The following imports are used in the setup.py file, so we can't remove them
# from here.
import re
import sys
#from setuptools import setup, find_packages
from setuptools import setup
from distutils.core import Extension
from distutils.command.build_ext import build_ext
from distutils.errors import (CCompilerError, DistutilsExecError,
                              DistutilsPlatformError)
from distutils.command.build import build
from distutils.command.clean import clean
from distutils.command.install_data import install_data
from distutils.command.install_lib import install_lib

# We import our version here to avoid circular imports.
from b3 import __version__

# ------------------------------------------------------------------------------
# Build extension modules
# ------------------------------------------------------------------------------

# The following code is based on the example at
# http://docs.python.org/2/distutils/apiref.html

class BuildFailed(Exception):
    pass


class ve_build_ext(build_ext):
    # This class allows C extension building to fail.

    def run
