import mmap
import os
import re
import sys

from . import _util
from . import _compat
from . import _winreg

# pylint: disable=too-few-public-methods
class _RegistryKey(object):
    """
    A context manager for the Windows registry.

    :param key:
        The registry key (one of the HKEY_* constants).
    :param sub_key:
        The name of the sub key.
    :param access:
        The desired access (defaults to KEY_READ).
    """
    def __init__(self, key, sub_key, access=_winreg.KEY_READ):
        self._key = key
        self._sub_key = sub_key
        self._access = access

    def __enter__(self):
        self._winreg_key = _winreg.OpenKey(self._key, self._sub_key, 0, self._access)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        _winreg.CloseKey(self._
