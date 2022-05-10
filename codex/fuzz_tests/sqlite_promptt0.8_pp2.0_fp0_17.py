import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
DATABASE = 'sensorDB'

# Regex for ipv4 and mac address
IPV4_REGEX = "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
MAC_REGEX = "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"

# Get libpcap using python
if platform.system() == 'Windows':
    ## Windows
    libpcap_path       = ctypes.util.find_msvcrt
