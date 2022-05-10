import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import string
import psutil

def get_pid(name):
    for proc in psutil.process_iter():
        try:
            if name.lower() in proc.name().lower():
                return proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None

if __name__ == '__main__':
    pid = get_pid("chrome")
    print("pid is: " + str(pid))
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    print(libc.syscall(186, pid, 1)) # 1 is read, 0 is write
