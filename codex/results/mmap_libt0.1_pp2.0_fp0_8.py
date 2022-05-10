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
from hashlib import md5
from HTMLParser import HTMLParser
from HTMLParser import HTMLParseError
from Queue import Queue
from Queue import Empty
from threading import Thread
from threading import Lock
from threading import Event
from threading import current_thread
from xml.etree import ElementTree

from resources.lib.utils import *
from resources.lib.utils import log
from resources.lib.utils import log_exception
from resources.lib.utils import log_error
from resources.lib.utils import log_debug
from resources.lib.utils import log_notice
from resources.lib.utils import log_warning
from resources.lib.utils import log_info
from resources.lib.utils import log_critical
from resources
