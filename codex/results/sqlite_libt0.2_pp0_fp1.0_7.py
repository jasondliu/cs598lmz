import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import signal
import subprocess
import re
import json
import traceback
import logging
import logging.handlers
import argparse
import socket

from datetime import datetime
from collections import OrderedDict

from . import config
from . import utils
from . import database
from . import logger
from . import __version__

# -----------------------------------------------------------------------------
#
# Global Variables
#
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#
# Functions
#
# -----------------------------------------------------------------------------

def parse_args():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Run the server')

    parser.add_argument('--config',
                        dest='config',
                        default=config.DEFAULT_CONFIG_FILE,
                        help='Configuration file')

    parser.add_argument('--log-file',
                        dest='log_file',
                        default=None,
                        help='Log file')

    parser.add_argument('--log-level',
                        dest='log_level',
                        default=
