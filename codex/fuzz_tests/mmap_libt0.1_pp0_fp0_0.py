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
from xml.dom import minidom

# Global variables
__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__addonname__ = __addon__.getAddonInfo('name')
__addonpath__ = __addon__.getAddonInfo('path')
__addonprofile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__addonicon__ = __addon__.getAddonInfo('
