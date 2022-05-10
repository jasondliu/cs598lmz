import lzma
lzma.open

# System imports
import os
import sys
import subprocess
import shutil
import tempfile
import re
import json
import time
import datetime
import argparse
import inspect
import traceback
import multiprocessing


# 3rd party imports
import requests

# Local imports
from . import util
from . import config
from . import __version__
from . import log
from . import exceptions
from . import update

_LOG = log.get_logger(__name__)


def ensure_dir(dir_name):
    """Check if directory exists, if not create it and its parents if needed."""
    if not os.path.exists(dir_name):
        _LOG.debug('Creating directory: %s', dir_name)
        os.makedirs(dir_name)


def ensure_file(file_name):
    """Check if file exists, if not create it and its parents if needed."""
    if not os.path.exists(file_name):
        _LOG.debug('Creating file: %s', file_name)
