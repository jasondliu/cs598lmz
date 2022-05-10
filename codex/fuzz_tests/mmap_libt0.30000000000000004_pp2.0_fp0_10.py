import mmap
import os
import re
import struct
import sys

from . import __version__
from . import _util
from . import _winreg
from . import _winreg_util

if sys.platform == 'win32':
    import _winreg
    import _winreg_util
    import _winreg_util_py2
    import _winreg_util_py3

# pylint: disable=too-few-public-methods
class _RegistryKey(object):
    """
    A class that represents a key in the registry.
    """
    def __init__(self, key):
        self._key = key

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '<_RegistryKey name="
