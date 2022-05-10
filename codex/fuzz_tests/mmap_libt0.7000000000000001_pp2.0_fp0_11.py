import mmap
import re
import sys
import time
import traceback
import unicodedata
from io import BytesIO
from textwrap import dedent

from . import (
    compat,
    exceptions,
    utils,
)

import six

if sys.version_info[0] == 2:
    import ConfigParser as configparser
else:
    import configparser

try:
    import win32api
except ImportError:
    win32api = None


class WinRMConfig(object):
    """
    Represents a Windows Remote Management configuration.

    In PowerShell, the WinRM configuration is stored in the registry.
    This class represents the on-disk configuration stored in the file
    C:\Windows\System32\WinRM\WinRM.config.

    The WinRM.config file can be read using the `Get-Content` PowerShell cmdlet,
    or by simply opening the file. The cmdlet reads the file using the
    encoding specified in the file header. If this is absent, the file is
    read using the system's current ANSI code page.

    If a file is opened using another
