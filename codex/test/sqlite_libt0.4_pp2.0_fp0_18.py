import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import argparse
import logging
import traceback
import json
import datetime
import socket
import struct

#
# NOTE: This is a modified version of the original script.
#
# The original can be found at:
# https://github.com/0xbb/wifi-probe-sniffer
#
# The original script was modified to work with Python 3.
#
# Changes:
# - Use bytes instead of str for data
# - Use bytes for MAC addresses
# - Use bytes for SSID
# - Use bytes for vendor
# - Use bytes for probe
# - Use bytes for beacon
# - Use bytes for payload
# - Use bytes for data
# - Use bytes for pkt_type
# - Use bytes for mac_addr
# - Use bytes for ssid
# - Use bytes for vendor
# - Use bytes for probe
# - Use bytes for beacon
# - Use bytes for payload
# - Use bytes for data
# - Use bytes for pkt_type
# - Use bytes for mac_addr
# - Use bytes for ssid
#
