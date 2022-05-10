import select
# Test select.select()
#
# This demo uses two sockets. One socket listens for data from any sender.
# The other socket sends data to the first socket.
#
# This demonstrates the use of select.select() to wait for data, as well
# as to wait for sockets to become writable.
#
# Illustrates the use of sockets, and the select module. 
#
# Uses the logging module to print messages to the console.
#
#   Python 3.3 Reference Library
#   http://docs.python.org/3.3/library/select.html
#   http://docs.python.org/3/howto/logging.html
#

import socket, logging
import time
from logging.handlers import TimedRotatingFileHandler
from threading import Timer
import os
from math import radians, cos, sin, asin, sqrt

from haversine import haversine
from random import random

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

import socket
import select
import sys
from udp_server import Message
