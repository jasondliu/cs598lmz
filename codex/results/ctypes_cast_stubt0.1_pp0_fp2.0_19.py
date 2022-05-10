import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 2

import os
import sys
import time
import logging
import threading
import traceback
import ctypes
import ctypes.util
import signal
import errno
import socket
import select
import struct
import fcntl
import platform
import subprocess
import weakref

from pypy.rpython.lltypesystem import rffi, lltype
from pypy.rpython.lltypesystem import ll2ctypes
from pypy.rpython.lltypesystem.lloperation import llop
from pypy.rpython.annlowlevel import llhelper
from pypy.rpython.annlowlevel import hlstr
from pypy.rpython.lltypesystem.rstr import STR
from pypy.rpython.lltypesystem.rstr import mallocstr
from pypy.rpython.lltypesystem.rstr import UNICODE
from pypy.rpython.lltypesystem.rstr import copystrtochar
from pypy.rpython.lltypesystem.
