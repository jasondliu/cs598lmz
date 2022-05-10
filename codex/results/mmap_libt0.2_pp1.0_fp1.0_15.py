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

# Plugin constants
__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonid__ = __addon__.getAddonInfo('id')
__addonpath__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__ = __addon__.getLocalizedString
__path__ = os.path.join(__addonpath__, 'resources', 'lib')
__path_img__ = os.path.join(__addonpath__, 'resources', 'media')

sys.path.append(__path__)

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import SoupStrainer

# Global variables

