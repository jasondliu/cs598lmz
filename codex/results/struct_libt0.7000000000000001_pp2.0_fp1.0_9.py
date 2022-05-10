import _struct
import _syscall
import ctypes
import ctypes.util
import errno
import functools
import os
import resource
import signal
import sys
import termios
import traceback

from ._util import _get_os_error


__all__ = [
    'set_terminal_size',
    'get_terminal_size',
    'set_terminal_cbreak',
    'set_terminal_cooked',
    'set_special_startup_mode',
    'set_blocking',
    'set_close_exec',
    'set_nonblocking',
    'set_inheritable',
    'set_startup_info',
    'get_startup_info',
    'set_process_groups',
    'set_signal_handlers',
    'set_subreaper',
    'get_subreaper',
    'get_process_groups',
    'get_terminal_attributes',
    'set_terminal_attributes',
    'get_signal_handlers',
    'set_in
