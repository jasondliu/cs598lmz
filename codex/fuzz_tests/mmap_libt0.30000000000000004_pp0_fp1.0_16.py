import mmap
import os
import re
import sys
import time

from datetime import datetime
from datetime import timedelta

# Constants

# Default values

# Globals

# Functions

def usage():
    print("Usage: {} [options]".format(sys.argv[0]))
    print("Options:")
    print("-h, --help     Print this usage message")
    print("-v, --verbose  Print verbose messages")
    print("-t, --trace    Print trace messages")

def main():
    global options

    # Parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvt", ["help", "verbose", "trace"])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-v",
