import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time
import datetime
import json
import re
import platform
import subprocess
import traceback
import urllib
import urllib2
import httplib
import socket
import base64
import shutil
import zipfile
import hashlib
import tempfile
import logging
import logging.handlers
import xml.etree.ElementTree as ET
import ConfigParser
import argparse
import platform

from lib.common import *
from lib.config import *
from lib.logger import *
from lib.db import *
from lib.daemon import *
from lib.updater import *
from lib.watcher import *
from lib.scanner import *
from lib.notifier import *
from lib.cleaner import *
from lib.web import *
from lib.api import *
from lib.utils import *

#-------------------------------------------------------------------------------
def main():
    # Initialize the logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create the console handler
    consoleHandler = logging.StreamHandler()
