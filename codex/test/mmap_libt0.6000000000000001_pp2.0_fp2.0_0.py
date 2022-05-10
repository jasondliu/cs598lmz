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

