import socket
socket.if_indextoname(3)

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     17/12/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import os
import time
import datetime
import StringIO
import subprocess
import struct
import socket
import re
import pcapy
import threading
import logging
import logging.handlers

from ctypes import *
from struct import *
from operator import attrgetter
from collections import defaultdict
from collections import namedtuple
from collections import Counter

#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Globals
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Helper Functions
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Classes
#-------------------------------------------------------------------------------

class flow():
    def __init__(self, src_ip, src_port, dst_ip, dst_port, proto, ts, pkt_len):
        self.src_ip = src_ip
        self.
