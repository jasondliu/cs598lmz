import mmap
import sys

import pytest

from pyglet.libs.win32 import _kernel32
from pyglet.libs.win32.constants import *
from pyglet.libs.win32.types import *

def test_CreateFile():
    handle = _kernel32.CreateFileW(
        'C:\\Windows\\System32\\notepad.exe',
        GENERIC_READ,
        FILE_SHARE_READ,
        None,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        None
    )
    assert handle != INVALID_HANDLE_VALUE
    _kernel32.CloseHandle(handle)

def test_CreateFileMapping():
    handle = _kernel32.CreateFileW(
        'C:\\Windows\\System32\\notepad.exe',
        GENERIC_READ,
        FILE_SHARE_READ,
        None,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        None
    )
    assert handle != INVALID_
