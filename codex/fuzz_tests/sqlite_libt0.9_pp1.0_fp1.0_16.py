import ctypes
import ctypes.util
import threading
import sqlite3


def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def get_libc():
    libc_path = which("libc.so.6")
    if libc_path:
        libc = ctypes.CDLL(libc_path)
    else:
        libc = ctypes.CDLL(ctypes.util.find_library("c"))
    return libc


def sync():
    libc = get_libc()
    r = libc.sync()
    return r


def drop_
