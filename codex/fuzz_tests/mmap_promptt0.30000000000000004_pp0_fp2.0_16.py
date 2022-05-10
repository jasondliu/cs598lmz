import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

import os
import sys
import time
import threading
import traceback
import logging
import logging.handlers
import signal
import subprocess
import socket
import struct
import shutil
import re

#
# Global constants
#

#
# Global variables
#

#
# Functions for the main program
#

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    global options, args

    #
    # Get the home directory for the user
    #
    homeDir = os.getenv("HOME")
    if homeDir == None:
        homeDir = os.getenv("USERPROFILE") # Windows
        if homeDir == None:
            usage("USERPROFILE environment variable not set")


