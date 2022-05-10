import lzma
lzma.LZMAFile #not in 2.6

import re
import sys
import os
import subprocess
import shutil
import logging

from . import VENDOR_PATH, TARGET_ARCH, TARGET_OS
from . import get_platform, get_python_version

def get_vendor_dir():
    return os.path.join(os.path.dirname(__file__), '..', VENDOR_PATH, TARGET_OS, TARGET_ARCH)

def get_vendor_lib_dir():
    return os.path.join(get_vendor_dir(), 'lib')

def get_vendor_bin_dir():
    return os.path.join(get_vendor_dir(), 'bin')

def get_vendor_include_dir():
    return os.path.join(get_vendor_dir(), 'include')

def get_vendor_pkgconfig_dir():
    return os.path.join(get_vendor_dir(), 'pkgconfig')

def get_vendor_share_dir():
   
