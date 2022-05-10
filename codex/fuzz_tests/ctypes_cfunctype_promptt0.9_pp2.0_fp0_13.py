import ctypes
# Test ctypes.CFUNCTYPE()
import os
import datetime
import time
import platform
import sys
import pathlib
import getpass
import primes

# Set the DLL search path to the same directory as this script
if platform.system() == 'Windows':
    os.add_dll_directory(os.path.dirname(os.path.abspath(__file__)))
else:
    os.environ["LD_LIBRARY_PATH"] = os.path.dirname(os.path.abspath(__file__))

# Set the C structures
class SessionInfo(ctypes.Structure):
    _fields_ = [
        ('app_id', ctypes.c_uint32),
        ('app_version', ctypes.c_float),
        ('export_name', ctypes.c_wchar_p),
        ('username', ctypes.c_wchar_p),
        ('computer', ctypes.c_wchar_p),
        ('client_name', ctypes.c_wchar_p),
        ('license', ctypes.c_wchar_p),
