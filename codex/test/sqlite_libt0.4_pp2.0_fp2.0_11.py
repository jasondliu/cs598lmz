import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import socket
import struct
import re

import dpkt
import dpkt.ethernet
import dpkt.ip
import dpkt.udp
import dpkt.tcp

import pcap

import mavlink

import logging

logging.basicConfig(level=logging.INFO)

# Need to figure out what we're running on
if os.name == 'nt':
    # Windows
    import win32api
    import win32con
    import win32security
    import win32file
    import pywintypes
    import winioctlcon
    import msvcrt
    import _winreg
    import wmi
    import win32net
    import win32netcon
    import win32event
    import win32process
    import win32service
    import win32serviceutil
    import win32api
    import win32con
    import win32security
    import win32file
    import pywintypes
    import winioctlcon
    import msvcrt
    import _win
