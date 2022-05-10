import socket
import sys
import os
import time
import datetime
import getpass
import ConfigParser
import pprint
import logging

from ctypes import *

from optparse import OptionParser

# Global variables

# Buffer for receiving data
g_buffer = 0

# Socket for communication
g_sock = 0

# Logging
g_loglevel = logging.WARNING
g_log = logging.getLogger('PacketSniffer')

# This is the packet structure we will receive
class Packet(Structure):
    _fields_ = [("ts", c_float),
                ("caplen", c_int),
                ("len", c_int),
                ("data", c_char * 4096)]

# The callback function
def packet_callback(ts, caplen, len, data, arg):
    global g_log
    global g_buffer

    if g_buffer > 0:
        if caplen > 0:
            g_log.debug("%s.%04d %d %d %s" % (datetime.datetime.utc
