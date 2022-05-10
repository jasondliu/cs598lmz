import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import scapy.all as scapy
from scapy.all import *

#import scapy_http.http as http
import time
import datetime
import json
import crc16

# https://stackoverflow.com/questions/22601082/how-to-disable-crc-check-in-scapy-layer-2
# https://scapy.readthedocs.io/en/latest/layers/checksum.html
# https://github.com/secdev/scapy/blob/master/scapy/layers/inet.py
# https://stackoverflow.com/questions/9505900/python-scapy-and-ethernet-checksum-calculation
# https://stackoverflow.com/questions/17393533/calculating-the-ether-type-field-on-an-ethernet-frame-using-scapy
# https://stackoverflow.com/questions/15305291/scapy-examples-of-ip-layer
# https://scapy.read
