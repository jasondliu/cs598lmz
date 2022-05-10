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

# Global variables
__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__author__ = __addon__.getAddonInfo('author')
__cwd__ = __addon__.getAddonInfo('path')
__date__ = __addon__.getAddonInfo('date')
__language__ = __addon__.getLocalizedString
__version__ = __addon__.getAddonInfo('version')
__resource__ = xbmc.translatePath(os.path.join(__cwd__, 'resources', 'lib'))
__settings__ = xbmcaddon.Addon(id='plugin.video.t
