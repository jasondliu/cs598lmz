import mmap
import os
import sys

from . import _compat
from . import _util
from . import _winreg


def _get_registry_value(hive, key, value=None):
    """Get a registry value from the specified hive and key.

    Args:
      hive: The registry hive to search.
      key: The registry key to search.
      value: The value to retrieve. If None, the default value will be returned.

    Returns:
      The value of the registry key.

    Raises:
      OSError: If the registry value cannot be retrieved.
    """
    try:
        handle = _winreg.OpenKey(hive, key)
    except WindowsError as e:
        raise OSError(e.errno, e.strerror)
    try:
        return _winreg.QueryValueEx(handle, value)[0]
    except WindowsError as e:
        raise OSError(e.errno, e.strerror)
    finally:
        _winreg.CloseKey(handle)


def _
