import socket
# Test socket.if_indextoname()

import os
import sys
import getopt
import string
import time
import struct
import array

import ifconfig
import ifconfig_util

def usage():
    print "Usage: %s [options] [interface]" % sys.argv[0]
    print "Options:"
    print "  -a, --all            show all interfaces"
    print "  -s, --stats          show interface statistics"
    print "  -r, --route          show the routing table"
    print "  -v, --verbose        be verbose"
    print "  -h, --help           show this help"
    print "  -V, --version        show version"

def version():
    print "ifconfig.py %s" % ifconfig.__version__
    print "Copyright (C) 1999-2001 by Erik Andersen <andersee@debian.org>"
    print "This program comes with NO WARRANTY, to the extent permitted by law."
    print "You may redistribute copies of this program"
    print "under the terms of the GNU General Public License."
    print "For
