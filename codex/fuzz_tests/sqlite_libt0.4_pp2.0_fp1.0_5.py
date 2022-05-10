import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import signal
import traceback
import serial
import serial.tools.list_ports
import json
import subprocess

# Global variables

# Serial port
ser = None

# Serial port lock
ser_lock = threading.Lock()

# Serial port read thread
ser_thread = None

# Serial port read thread exit flag
ser_thread_exit = False

# Serial port read thread
def ser_thread_run():
    global ser_thread_exit
    while not ser_thread_exit:
        # Read serial port
        ser_lock.acquire()
        try:
            # Read from serial port
            line = ser.readline()
        except:
            # Serial port error
            line = None
        ser_lock.release()
        # Check for serial port error
        if line == None:
            # Serial port error
            break
        # Check for exit
        if ser_thread_exit:
            break
        # Check for empty line
        if len(line) == 0:
            continue
        # Check for line length
