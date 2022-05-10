import ctypes
ctypes.cast(ctypes.c_void_p(1), ctypes.c_void_p)

# imports

import sys
import os
import shutil
import re

import ctypes.util
import ctypes
import ctypes.wintypes
import json

# constants

MEMORY_BASIC_INFORMATION = ctypes.wintypes.DWORD * 7

# utilities

def ida_version():
    return sys.modules["__main__"].idaapi.IDA_SDK_VERSION

def ida_version_major():
    return sys.modules["__main__"].idaapi.IDA_SDK_VERSION // 10000

def ida_version_minor():
    return sys.modules["__main__"].idaapi.IDA_SDK_VERSION // 100 % 100

def ida_version_patch():
    return sys.modules["__main__"].idaapi.IDA_SDK_VERSION % 100

