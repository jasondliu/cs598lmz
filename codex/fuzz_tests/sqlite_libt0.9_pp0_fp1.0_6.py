import ctypes
import ctypes.util
import threading
import sqlite3
import StringIO
import sys

def printse(*args):
    print >> sys.stderr, args
def prints(*args):
    print >> sys.stdout, args

def init_if(if_name, start=None, end=None):
    local_ip = "0.0.0.0"
    libnet = ctypes.cdll.LoadLibrary(ctypes.util.find_library("net"))

    subnet = '255.255.255.255'
    arp_addr = '192.168.1.12'
    subtype = 8
    out = StringIO.StringIO()

    def printsystem(type, value, tb):
        out.write('***' * 10)
        out.write('Fatal Python error: %s' % type.__name__)
        out.write(str(value))
        printout(out)
        sys.__excepthook__(type, value, tb)
    sys.excepthook = printsystem

    while True:
        try:
            db = sqlite
