import ctypes
import ctypes.util
import threading
import sqlite3
import subprocess
import time
import os
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import socket
import getpass
import platform
import netifaces

global HOSTNAME
global IP_ADDRESS
global USERNAME
global OS
global INTERFACE
global INTERFACE_ADDR
global INTERFACE_BROADCAST

HOSTNAME = socket.gethostname()
USERNAME = getpass.getuser()
OS = platform.system()

if __name__ == "__main__":
    if "Linux" == OS:
        INTERFACE = netifaces.gateways()['default'][2][1]
        INTERFACE_ADDR = netifaces.ifaddresses(INTERFACE)[netifaces.AF_INET][0]['addr']
        INTERFACE_BROADCAST = netifaces.ifaddresses(INTERFACE)[netifaces.AF_INET][0]['broadcast']
    else:
        INTERFACE = "en0"
