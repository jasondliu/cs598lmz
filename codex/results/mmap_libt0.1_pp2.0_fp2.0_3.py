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
from HTMLParser import HTMLParser
from HTMLParser import HTMLParseError
from Queue import Queue
from Queue import Empty
from threading import Thread
from threading import Lock
from threading import Event
from threading import Condition
from threading import current_thread
from threading import active_count

from resources.lib.common import *
from resources.lib.common import log
from resources.lib.common import notify
from resources.lib.common import get_credentials
from resources.lib.common import get_credentials_v2
from resources.lib.common import get_credentials_v3
from resources.lib.common import get_credentials_v4
from resources.lib.common import get_credentials
