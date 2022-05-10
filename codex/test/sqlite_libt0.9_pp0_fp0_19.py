import ctypes
import ctypes.util
import threading
import sqlite3
import time
import tkinter.messagebox

from queue import Queue

from pytube import YouTube

def get_exec_dir():
    """ <py2exe> get_exec_dir() Returns the directory where the executable is running from.
        Returns: string -- dir to the directory """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.realpath(__file__))

def get_exec_path():
    """ <py2exe> get_exec_path() Returns the path of the executable running.
        Returns: string -- filepath to the executable """
    if getattr(sys, 'frozen', False):
        return sys.executable
    return os.path.realpath(__file__)

if getattr(sys, 'frozen', False):  # bundlemode
    # change cwd to bundle directory to prevent sys._MEIPASS error
    os.chdir(get_exec_dir())
