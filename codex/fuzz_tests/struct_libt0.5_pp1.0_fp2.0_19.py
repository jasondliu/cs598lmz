import _struct
import _thread
import _threading_local
import _warnings
import _weakref
import array
import atexit
import audioop
import binascii
import builtins
import cmath
import errno
import fcntl
import gc
import grp
import itertools
import marshal
import math
import mmap
import operator
import os
import parser
import resource
import select
import shlex
import shutil
import signal
import socket
import stat
import string
import struct
import subprocess
import sys
import sysconfig
import tempfile
import time
import timeit
import traceback
import unicodedata
import zipimport

# Note: _thread is NOT frozen, unlike _threading_enums

# Embedders should also freeze sys.flags, sys.float_info, sys.hash_info,
# sys.int_info, and sys.version_info.  (Perhaps that should be done here.)

# XXX Should we freeze sys.builtin_module_names?

# XXX Should we try to freeze sys.abiflags?

#
