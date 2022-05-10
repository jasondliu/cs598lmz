import types
types.ModuleType.__getattr__ = lambda self, key: self.__dict__.get(key, None)
import urllib2
from xml.dom import minidom
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmcvfs
import traceback
from HTMLParser import HTMLParser
from datetime import datetime
import re
import os
import sys
import time
from threading import Thread
from Queue import Queue

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

try:
    from sqlite3 import dbapi2 as sqlite
except:
    from pysqlite2 import dbapi2 as sqlite

if sys.version_info < (2, 7):
    import simplejson
else:
    import json as simplejson

from metahandler import metahandlers

from resources.lib import utils
from resources.lib.utils import *
from resources.lib.playback import *
