import ctypes
import ctypes.util
import threading
import sqlite3
import json
import inspect
import sys
import os
import psutil
import platform

win_sys_path = "C:\\Windows\\system32"
win_sys_alt = "C:\\WinNT\\system32"
win_sys_x64 = "C:\\Windows\\syswow64"

win_explorer_exe = None

arch = platform.architecture()[0]

py_path = os.path.dirname(inspect.getfile(inspect.currentframe()))
py_path = py_path.replace("\\", "/")
lib_arr = py_path.split("/")
if (lib_arr[0] == 'C:'):
	del lib_arr[0]
lib_path = "/".join(lib_arr)

del lib_arr[0]

lib_path = "/".join(lib_arr)
cef_wtf_lib_path = os.getcwd().replace("\\", "/") + "/lib/cef_wtf.dll"

if not os.path.exists(cef
