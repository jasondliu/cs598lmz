import ctypes
import ctypes.util
import threading
import sqlite3
import os
import subprocess
from multiprocessing import Process
import logging
import time
import platform
from common import log_exceptions, save_to_file, get_cpu_percent, get_cpu_times, get_memory_percent, get_process_info, get_disk_usage, get_network_info, get_hostname, get_current_time, get_battery_params
from common import get_temperature, get_fan_speed
import json
import sys

if platform.system() == "Darwin":
    sys.path.append('/usr/local/lib/python2.7/site-packages')

import psutil

class Client(threading.Thread):

    def __init__(self, server, port, timeout, sleep_time=3):

        self.process = threading.Thread.__init__(self)

        self.server = server
        self.port = port
        self.timeout = timeout
        self.sleep_time = sleep_time

        self.db = sqlite3.connect('monitor.sqlite')
        self.cur
