import mmap
import os
import random
import select
import signal
import socket
import struct
import sys
import threading
import time
import traceback
import urllib
import urllib2
import zlib

import xlog

current_path = os.path.dirname(os.path.abspath(__file__))

root_path = os.path.abspath( os.path.join(current_path, os.pardir, os.pardir))
data_path = os.path.abspath(os.path.join(root_path, os.pardir, os.pardir, 'data'))

sys.path.append(root_path)

import simple_http_server

if not os.path.isdir(data_path):
    data_path = current_path

logging_level = logging.INFO

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(module)s.%(funcName)s
