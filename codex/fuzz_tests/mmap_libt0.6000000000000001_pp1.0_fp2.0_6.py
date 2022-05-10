import mmap
import re
import signal
import socket
import sys
import time
import argparse

from collections import deque
from datetime import datetime
from email.mime.text import MIMEText
from email.utils import formatdate
from functools import partial
from hashlib import md5
from itertools import imap
from multiprocessing import Pool, cpu_count
from os import getpid, kill, path, system
from random import choice
from subprocess import Popen, PIPE
from textwrap import TextWrapper
from threading import Thread, Event
from xml.dom.minidom import Document, parseString

# local imports
from version import version as __version__

# local imports
from version import version as __version__


# ------------------------------------------------------------------------------
# globals
# ------------------------------------------------------------------------------

# merge multiple log files into one stream
merge = False

# use mmap() to read files
mmap = False

# use the tail program to read files
tail = False

# use the tail program to read files
tail_args = []

# use the tail program to
