import ctypes
import ctypes.util
import threading
import sqlite3
import traceback

IRC_CHANNEL = "#smoothstreams"

_libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

_gameMachine_pid = 0

def _get_proc_stats(pid):
    """
    Return stats of process pid as a list of tuples.
    """

    stats = file('/proc/%d/stat' % (pid,)).read()
    stats = stats[stats.index(')') + 2:].split()

