import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import time
import datetime
import shutil
import subprocess
import tempfile
import logging
import logging.handlers
import argparse
import urllib
import urllib2
import json
import socket
import threading
import Queue
import traceback
import ConfigParser
import platform
import ctypes
import ctypes.util

from pprint import pprint

#-------------------------------------------------------------------------------
# Global variables
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Global functions
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Classes
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('-c', '--config', dest='config', help='config file', default='config.ini')
    parser.add_argument('-l', '--log', dest='log', help='log file', default='log.txt
