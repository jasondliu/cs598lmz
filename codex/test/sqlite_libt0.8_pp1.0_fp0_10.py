import ctypes
import ctypes.util
import threading
import sqlite3
import fcntl

'''
ckpt = ctypes.CDLL("./libckpt.so", mode=ctypes.RTLD_GLOBAL)

def _to_pid(pid):
    try:
        pid = int(pid)
    except:
        pid = int(subprocess.check_output(['pidof', '-s', pid]).strip())

    return pid

def resume(pid, flags, status):
    return ckpt.resume(_to_pid(pid), flags, status)

def ckpt_suspend(pid, flags):
    return ckpt.checkpoint(_to_pid(pid), flags)

def ckpt_kill(pid, flags):
    return ckpt.kill(_to_pid(pid), flags)

def ckpt_restart(pid, status, flags):
    return ckpt.restart(_to_pid(pid), status, flags)
'''

