import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from dateutil import parser
from dateutil import tz
from dateutil.relativedelta import relativedelta
from HTMLParser import HTMLParser
from HTMLParser import HTMLParseError
from Queue import Queue
from Queue import Empty
from threading import Thread
from threading import Lock
from threading import Event
from threading import Condition
from xml.etree import ElementTree

try:
    import StorageServer
except:
    import storageserverdummy as StorageServer

try:
    import json
except:
    import simplejson as json

try:
    import CommonFunctions
except:
    import commonfunctionsdummy as CommonFunctions

try:
    import StorageServer
except:
    import st
