import lzma
lzma.open

import os
import sys
import time
import re
import json
import gzip
import bz2
import datetime
import tempfile
import shutil
import subprocess

from functools import wraps
from itertools import islice
from collections import defaultdict
from contextlib import contextmanager

from . import util

import logging
logger = logging.getLogger(__name__)

def run_cmd(cmd, *args, **kwargs):
    """Execute a command"""
    logger.debug("Running: %s %s %s" % (cmd, args, kwargs))
    output = subprocess.check_output([cmd] + list(args), **kwargs)
    stdout = output.decode('utf-8')
    logger.debug("Returned: %s" % stdout)
    return stdout

class FileNotFound(Exception):
    pass

class FileFormat(object):
    """
    Base class for file formats
    """
    def __init__(self, fname, **kwargs):
       
