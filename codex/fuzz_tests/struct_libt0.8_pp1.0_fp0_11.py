import _struct
import _thread
import _threading
import time
import _time
import _weakref

try:
    import _winapi
except ImportError:
    pass


if platform.python_implementation() == "CPython":
    import _curses
    import _curses_panel
    import fcntl
    import grp
    import mmap
    import nis
    import readline
    import resource
    import syslog
    import termios
    import zlib
else:
    import _curses
    import _curses_panel
    import _multiprocessing

import os
import select
import signal
import subprocess
import sys
import sysconfig
import syslog
import tempfile
import getpass

# All the modules that the platform supports
SUPPORTED_PLATFORM_MODULES = [
    "array",
    "cmath",
    "math",
    "errno",
    "fcntl",
    "select",
    "signal",
    "sys",
    "time",
    "thread",
    "
