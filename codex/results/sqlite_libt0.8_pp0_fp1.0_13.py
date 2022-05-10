import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys

try:
    import pyinotify
except:
    print("[-] pyinotify not found.")
    print("[-] Please install it:")
    print("[-] sudo pip install pyinotify")
    sys.exit(-1)

try:
    import hashlib
    md5 = hashlib.md5
except ImportError:
    print("[-] hashlib not found.")
    print("[-] Please install it:")
    print("[-] sudo apt-get install python-dev")
    print("[-] sudo pip install hashlib")
    sys.exit(-1)

#
# @return an array of the size of the files in the directory
#
def get_files(directory):
    return os.scandir(directory)

#
# @return a boolean that indicates if the file specified by path exists
#
def file_exists(path):
    try:
        if os.path.exists(path):
            return True
    except FileNotFoundError:
       
