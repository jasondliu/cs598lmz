import _struct
import ctypes
from ctypes import wintypes
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPCWSTR, LPVOID, LPWSTR

from pywintypes import error

from win32 import win32api
from win32 import win32con
from win32.lib import kernel32
from win32.lib import advapi32
from win32.lib import shell32
from win32.lib import user32
from win32.lib import shlwapi
from win32.lib import wtsapi32
from win32.lib import netapi32
from win32.lib import crypt32
from win32.lib import mpr
from win32.lib import winnetwk
from win32.lib import userenv
from win32.lib import netapi32
from win32.lib import dwmapi
from win32.lib import setupapi
from win32.lib import shell32

from win32.lib.kernel32 import (
    CloseHandle,
    CopyFileW,
    CreateDirectoryW,
    CreateFileW,
    CreateHardLinkW
