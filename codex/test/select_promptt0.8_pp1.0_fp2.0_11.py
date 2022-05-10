import select
# Test select.select
from time import time
from lib import *

from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, \
    SOL_SOCKET, SO_REUSEADDR, IPPROTO_IP, IP_ADD_MEMBERSHIP, \
    inet_aton, gethostbyname

from threading import Thread

from getopt import getopt, gnu_getopt
from sys import argv, exit, stdout, stderr
from os import environ
from os.path import basename
from errno import EINTR

from math import log10
from random import randrange

from ppi import g_endian, W_LITTLE_ENDIAN, W_BIG_ENDIAN

# FIXME: Just for testing!
from array import array
#from Numeric import array

# FIXME: for now, need a global storage for global context
from ppi.dbm import g_dbm

from ppi import ppi_fixed, ppi_var, ppi_proto, ppi_proto
