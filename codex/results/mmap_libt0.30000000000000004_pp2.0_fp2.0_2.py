import mmap
import os
import sys
import time

from . import _common
from . import _constants
from . import _errors
from . import _util
from . import _winreg

# pylint: disable=protected-access

if sys.platform == 'win32':
  import _winapi
  import msvcrt

  # pylint: disable=invalid-name
  _CreateFile = _winapi.CreateFile
  _CloseHandle = _winapi.CloseHandle
  _ReadFile = _winapi.ReadFile
  _WriteFile = _winapi.WriteFile
  _SetFilePointer = _winapi.SetFilePointer
  _GetFileSize = _winapi.GetFileSize
  _GetFileType = _winapi.GetFileType
  _GetFileInformationByHandle = _winapi.GetFileInformationByHandle
  _GetFileAttributes = _winapi.GetFileAttributes
  _SetFileAttributes = _winapi.SetFileAttributes
  _SetEndOfFile = _winapi.SetEndOfFile
  _GetFileTime = _winapi
