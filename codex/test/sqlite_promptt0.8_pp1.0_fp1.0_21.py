import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/opt/selene/data/selene.db')
import os.path
import socket
import errno
import traceback
import sqlite3
import sys
import os
import shutil
#import qhue
import json
import urllib.request
import pathlib
import typing
import re

from selene_sdk.sdk import SeleneSdk, SeleneSdkEvent
from selene_sdk.__init__ import __version__

_logger = logging.getLogger(__name__)

SELENE_HOME = os.environ.get("SELENE_HOME", '/opt/selene')

# Default configuration.
