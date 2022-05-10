import gc, weakref
import os
import StringIO
import gzip

from ctypes import *
import ctypes
import gc, weakref



import struct
import sys
import traceback
import os
import time
import math



class _Proc(object):
    def __init__(self, name, pid):
        self._name = name
        self._pid = pid
        self._is_info_loaded = False
        self._is_dwarf_loaded = False
        self._is_libs_loaded = False
        self._is_modules_loaded = False
        self._is_regs_loaded = False
        self._is_threads_loaded = False
        self._is_maps_loaded = False
        self._is_shared_loaded = False
        self._is_fds_loaded = False
        self._is_thread_groups_loaded = False
        self._is_modules_loaded = False
        self._is_core_loaded = False
        self._is_core_file_loaded = False
        self._is_core_info_loaded = False
       
