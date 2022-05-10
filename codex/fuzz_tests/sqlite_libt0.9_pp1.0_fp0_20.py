import ctypes
import ctypes.util
import threading
import sqlite3
import gc
import traceback
import os.path


def find_libpcre():
  lib_names = ['libpcre.so.3']
  if 'linux' in platform.system().lower():
    lib_names.append('libpcre.so')
  elif 'darwin' in platform.system().lower():
    lib_names.append('libpcre.dylib')
  for lib_name in lib_names:
    lib_path = os.path.join('/', 'lib', lib_name)
    if os.path.exists(lib_path):
      return ctypes.cdll.LoadLibrary(lib_path)
  lib_path = ctypes.util.find_library("pcre")
  if lib_path is None:
    raise ImportError("Failed to find libpcre")
  return ctypes.cdll.LoadLibrary(lib_path)

class Patterns:

  BYTE = b'BYTE'
  TEXT = b'TEXT'
  PCRE = b'PCRE'
  BYTE_IGNORECASE =
