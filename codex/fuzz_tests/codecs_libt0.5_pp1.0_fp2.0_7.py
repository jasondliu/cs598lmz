import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import socket
import struct
import random
import string
import logging
import logging.handlers
import argparse
import multiprocessing
import subprocess
import threading

from datetime import datetime, timedelta
from collections import OrderedDict

from lib import *

# Global variables
#
#

# Python 2.x
if sys.version_info[0] < 3:
    import ConfigParser as configparser
    from Queue import Queue
    from StringIO import StringIO
# Python 3.x
else:
    import configparser
    from queue import Queue
    from io import StringIO

#
#
# Global variables

# Version
VERSION = '1.1.2'

# Logger
logger = None

# Config
config = None

# Processes
processes = []

# Processes
processes_lock = threading.Lock()

# Processes

