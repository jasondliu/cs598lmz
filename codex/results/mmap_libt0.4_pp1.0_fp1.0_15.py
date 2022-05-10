import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

from collections import defaultdict
from datetime import datetime
from itertools import product

from . import utils

logger = logging.getLogger(__name__)

def _create_temp_dir():
    return tempfile.mkdtemp(prefix='py-spy-')

def _create_temp_file():
    fd, path = tempfile.mkstemp(prefix='py-spy-')
    os.close(fd)
    return path

def _get_temp_dir():
    """
    Return the path to a temporary directory.

    The directory is created if it does not exist.
    """
    path = os.environ.get('PYSPY_TEMP_DIR')
    if path is None:
        path = _create_temp_dir()
    else:
        if not os.path.exists(path):
            os.makedirs(path)
    return path

def _get_temp_
