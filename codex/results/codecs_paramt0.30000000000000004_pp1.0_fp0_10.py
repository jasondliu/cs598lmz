import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import glob
import re
import urllib
import urllib2
import json
import time
import random
import logging
import logging.handlers
import datetime
import subprocess
import traceback
import unicodedata
import threading
import Queue

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs

# Import the common settings
from settings import Settings
from settings import log
from settings import os_path_join
from settings import os_path_split
from settings import os_path_isdir
from settings import os_path_exists
from settings import os_path_split
from settings import os_path_basename
from settings import os_path_dirname
from settings import os_path_join
from settings import os_path_split
from settings import os_path_splitext
from settings import os_path_abspath
from settings import os_path_normpath
from settings import os_path_expanduser
from settings
