import mmap
import os
import sys
import time
import traceback

from collections import deque
from datetime import datetime
from functools import partial
from multiprocessing import Pool, cpu_count
from os.path import dirname, join, exists
from random import choice
from shutil import rmtree
from subprocess import Popen, PIPE, STDOUT

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

