import _struct
import glob
import numpy
import os
import re
import socket
import struct
import sys
import optparse
import tempfile

parser = optparse.OptionParser()
parser.set_usage(
"python wms_read_wmm.py [options]\n"
"\n")
parser.add_option("-u", "--update", dest="update",
                  help="Update the file", action="store_true",
                  default=False)

(options, args) = parser.parse_args()

def index(a, b):
    return a[0].index(b)

def search(a, b):
    if b in a[0]:
        return a[0].index(b)
    return -1

def extraction(a):
    if sys.version_info.major == 2:
        return a[1:].replace(' ', '_').strip('"'), a[0].split()
    return a[1:].replace(' ', '_').strip('"').decode('utf8'), a[0].split()

