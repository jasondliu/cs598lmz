import ctypes
import ctypes.util
import threading
import sqlite3
import os
import io
import sys
import subprocess
import re
import fnmatch
import inspect
import time
import copy
import magic

from hdfs3 import HDFileSystem

sigaction = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True).sigaction
sig_ignore = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_void_p)
_SIG_IGNORE = sig_ignore(ctypes.c_int(0))

def _sig_ignore_wrapper(signal_to_ignore, only_in_thread_id=None):
    """
    Prevent crashing from SIGPIPE when a client disconnects.
    :param signal_to_ignore: The signal to ignore.
    """
    if only_in_thread_id is None or threading.get_ident() == only_in_thread_id:
        sigaction(signal_to_ignore, _SIG_IGNORE, None)
