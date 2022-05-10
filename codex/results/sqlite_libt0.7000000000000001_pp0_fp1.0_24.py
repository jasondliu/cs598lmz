import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import stat
import random
import re
import string
import json
import logging
import logging.handlers
import traceback
import sys
import BaseHTTPServer
import urllib2
import zipfile

from os import path
from os.path import isdir, isfile
from xml.dom import minidom
from subprocess import Popen, PIPE, STDOUT
from simplejson import dumps
from datetime import datetime
from random import choice
from copy import deepcopy
from datetime import datetime

import config
import util
import files
import updater

# -----------------------------------------------------------------------------

class TMDb(object):
    def __init__(self):
        self._api_key = None
        self._API_URL = 'http://api.themoviedb.org/2.1/'
        self._API_KEY_URL = 'http://api.themoviedb.org/2.1/Movie.getAPIKey/'
        self._API_KEY_PARAMS = '?id=%s&time=%s&hash
