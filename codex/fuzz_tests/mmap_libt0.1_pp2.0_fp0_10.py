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

from resources.lib.utils import *
from resources.lib.utils import log
from resources.lib.utils import logDbg
from resources.lib.utils import logErr
from resources.lib.utils import logWarn
from resources.lib.utils import logNotice
from resources.lib.utils import logInfo
from resources.lib.utils import logDebug
from resources.lib.utils import logError
from resources.lib.utils import logWarning
from resources.lib.utils import logNotice
from resources.lib.utils import logInfo
from
