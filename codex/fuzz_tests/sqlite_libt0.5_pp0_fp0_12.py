import ctypes
import ctypes.util
import threading
import sqlite3
import json
import os
import sys
import time
import traceback
import random
import platform
import fcntl
import struct
import socket
import array
import subprocess
import datetime
import tempfile
import shutil
import re
import logging

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from . import config
from . import util
from . import zeroconf
from . import log
from . import version

logger = logging.getLogger(__name__)

if sys.version_info[0] < 3:
    import ConfigParser as configparser
else:
    import configparser

if sys.version_info[0] >= 3:
    # Python 3
    import urllib.parse as urlparse
    from urllib.parse import quote_plus
    from urllib.parse import urlencode
    import urllib.request as urllib_request
else:
    # Python 2
    import urlparse
    from urllib import quote_plus

