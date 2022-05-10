from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = _bz2_decompress

from shlex import split
from subprocess import Popen, PIPE, STDOUT

from collections import defaultdict
from collections import deque

from functools import partial

from os import makedirs, chdir, getcwd, path, rename
from sys import argv, stdout, stderr

import pickle

from time import time, sleep

from platform import system as system_platform

from numpy import mean

from multiprocessing import Pool, cpu_count

from xmlrpc.client import ServerProxy

from hashlib import md5

from datetime import datetime

from copy import copy

import re

from itertools import cycle

from urllib.parse import urlparse

from urllib.request import urlopen


"""

Pygmy is a small tool for managing and running a distributed computing cluster
with a single command line.

"""


# Pygmy version
pygmy_version = "1.0.0"

# Pygmy version

