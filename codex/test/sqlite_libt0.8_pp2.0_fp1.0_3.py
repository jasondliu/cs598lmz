import ctypes
import ctypes.util
import threading
import sqlite3
import requests
import bs4
import re
import os
import inspect
import time
import sys

def terminal_size():
    current_os = platform.system()
    tuple_xy = None

    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()

        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()

            if tuple_xy is None:
                tuple_xy = _get_terminal_size_linux()

    else:
        tuple_xy = _get_terminal_size_linux()

    if tuple_xy is None:
        return (80, 25)

    return tuple_xy

