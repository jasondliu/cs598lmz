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

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

# Global Variables
ADDON_ID = 'plugin.video.nhl'
ADDON = xbmcaddon.Addon(ADDON_ID)
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_PATH = ADDON.getAddonInfo('path').decode('utf-8')
ADDON_VERSION = ADDON.getAddonInfo('version')
ICON = ADDON.getAddonInfo('icon')
FANART = ADDON.getAddonInfo('fanart')
LANGUAGE = ADDON.getLocalizedString

DEBUG = ADDON.getSetting('debug')

BASE_URL = 'http://video.nhl.com'
BASE_URL_OLD = 'http://video.nhl.com
