import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import subprocess
import signal
import re

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

sys.stdout = Logger("log.txt")

def get_pid(name):
    return map(int,subprocess.check_output(["pidof",name]).split())

def kill_pid(pid):
    os.kill(pid, signal.SIGKILL)

def kill_process(name):
    for pid in get_pid(name):
        kill_pid(pid)

def get_process_status(name):
    return len(get_pid(name))

def get_process_status_pid(pid):
    try:
        os.kill(pid, 0)
        return True
    except OSError:
