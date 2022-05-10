import mmap
import subprocess
import ctypes
import ctypes.wintypes

from os import path
from os import SEEK_SET
from subprocess import PIPE
from tempfile import TemporaryFile
from threading import Thread
from ctypes.wintypes import DWORD
from ctypes.wintypes import LPCVOID
from ctypes.wintypes import BOOL
from ctypes.wintypes import LPVOID
from ctypes.wintypes import LPCSTR
from ctypes.wintypes import HANDLE
from ctypes.wintypes import HINSTANCE
from ctypes.wintypes import LPWSTR
from ctypes.wintypes import LPCWSTR
from ctypes.wintypes import LPBYTE
from ctypes.wintypes import LPDWORD
from ctypes.wintypes import LPVOID
from ctypes.wintypes import HMODULE
from ctypes.wintypes import FARPROC
from ctypes.wintypes import UINT
from ctypes.wintypes import WORD

from ctypes import windll
from ctypes import
