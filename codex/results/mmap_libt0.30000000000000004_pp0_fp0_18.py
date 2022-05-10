import mmap
import os
import re
import subprocess
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from multiprocessing import Process, Queue
from optparse import OptionParser
from pprint import pprint
from random import randint
from shutil import copyfile
from subprocess import Popen, PIPE
from threading import Thread
from time import sleep

# disable buffering
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# global variables
options = None
args = None

# constants
NUM_THREADS = 10
NUM_PROCESSES = 10

# global variables
options = None
args = None

# constants
NUM_THREADS = 10
NUM_PROCESSES = 10

# global variables
options = None
args = None

# constants
NUM_THREADS = 10
NUM_PROCESSES = 10

# global variables
options = None
args = None

# constants
NUM_THREADS = 10
NUM_PR
