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
__plugin__ = "plugin.video.nhl"
__author__ = "NHL"
__url__ = "http://www.nhl.com"
__settings__ = xbmcaddon.Addon(id=__plugin__)
__language__ = __settings__.getLocalizedString
__version__ = __settings__.getAddonInfo('version')
__profile__ = xbmc.translatePath(__settings__.getAddonInfo('profile'))
__resource__ = xbmc.translatePath(os.path.join(__settings__.getAddonInfo('path'), 'resources', 'lib'))
__temp__ = xbmc.translatePath(os.path.join(__profile__, 'temp', ''))

