import socket
import time
import threading
import sys
import os
import signal
import logging
import logging.handlers
import argparse
import multiprocessing
import Queue
import re
import select

# create logger
logger = logging.getLogger('SOCKS5_SERVER')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.handlers.RotatingFileHandler('SOCKS5_SERVER.log', maxBytes=1024*1024*100, backupCount=5)
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler
