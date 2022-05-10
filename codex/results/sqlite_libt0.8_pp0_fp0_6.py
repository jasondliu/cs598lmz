import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import logging
import sys
import tempfile
import urllib
import shutil
import socket

from base64 import b64decode
from random import choice
from datetime import datetime
from functools import partial
from subprocess import check_output, PIPE
from os.path import exists
from binascii import hexlify, unhexlify
from socket import gethostname

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from electrum_twisted import bitcoin
from electrum_twisted.i18n import _
from electrum_twisted.util import format_satoshis

from electrum_twisted_gui.qt.util import *
from electrum_twisted_gui.util import *
from electrum_twisted_gui.plugin import run_hook
from electrum_twisted_gui.bitcoin import COIN

from electrum_twisted.plugins import BasePlugin

logger = logging.getLogger(__name__)

# Filter for EAN
