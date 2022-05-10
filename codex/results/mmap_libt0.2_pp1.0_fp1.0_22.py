import mmap
import os
import sys
import time

from . import _util
from . import _winreg

_winreg_HKEY_LOCAL_MACHINE = _winreg.HKEY_LOCAL_MACHINE
_winreg_HKEY_CURRENT_USER = _winreg.HKEY_CURRENT_USER

_winreg_KEY_READ = _winreg.KEY_READ
_winreg_KEY_WRITE = _winreg.KEY_WRITE
_winreg_KEY_ALL_ACCESS = _winreg.KEY_ALL_ACCESS

_winreg_REG_SZ = _winreg.REG_SZ
_winreg_REG_DWORD = _winreg.REG_DWORD
_winreg_REG_BINARY = _winreg.REG_BINARY
_winreg_REG_MULTI_SZ = _winreg.REG_MULTI_SZ
_winreg_REG_EXPAND_SZ = _winreg.REG_EXPAND_SZ
_winreg_REG_NONE = _winreg.REG
