import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import re
import time
import shutil
import subprocess
import logging
import logging.handlers
import argparse
import json
import threading
import socket
import fcntl
import errno
import codecs

#
# Globals
#

#
# Logging
#

class Logger:
    def __init__(self, log_file):
        self.logger = logging.getLogger('server')
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False

        # create file handler which logs even debug messages
        fh = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        self.logger.addHandler(
