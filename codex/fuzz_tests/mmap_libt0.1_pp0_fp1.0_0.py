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

from BeautifulSoup import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from HTMLParser import HTMLParser
from HTMLParser import HTMLParseError
from StringIO import StringIO
from threading import Thread
from threading import Lock
from threading import Condition
from threading import Event
from threading import currentThread
from xml.dom.minidom import parseString

__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__addonname__ = __addon__.getAddonInfo('name')
__addonpath__ = __addon__.getAddonInfo('path')
__addonprofile__ = __addon__.getAddonInfo('profile')
__addonicon__ =
