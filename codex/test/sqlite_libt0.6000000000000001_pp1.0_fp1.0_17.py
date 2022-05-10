import ctypes
import ctypes.util
import threading
import sqlite3
import os
import gc
import subprocess
import uuid
import signal
import time
from datetime import datetime
import sys
import argparse
from multiprocessing import Process
import random

# Set up logger
log = logging.getLogger('pythontest')
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

# Set up argparser
parser = argparse.ArgumentParser(description='Python test suite.')
parser.add_argument('--suite', help='Run a specific test suite', required=False)
parser.add_argument('--num-threads', help='Number of threads to start', required=False, default=1, type=int)
parser.add_argument('--num-processes', help='Number of processes to start', required=False, default=1, type=int)
parser.add_argument('--num-runs', help='Number of times to run each test', required=False, default=1, type=int)
