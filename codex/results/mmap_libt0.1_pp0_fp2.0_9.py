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
from httplib import BadStatusLine
from httplib import IncompleteRead
from httplib import HTTPException
from Queue import Queue
from Queue import Empty
from threading import Thread
from threading import Lock
from threading import Event
from threading import current_thread
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError

from resources.lib.common import log
from resources.lib.common import notify
from resources.lib.common import settings
from resources.lib.common.exceptions import AbortException
