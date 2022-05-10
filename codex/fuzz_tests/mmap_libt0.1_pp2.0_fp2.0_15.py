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
__addonversion__ = __addon__.getAddonInfo('version')
__addonname__ = __addon__.getAddonInfo('name')
__addonpath__ = __addon__.getAddonInfo('path')
__addonprofile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__addonicon__ = xbmc.translatePath(os.path.join(__addonpath__, 'icon.png'))
__addonfanart__ = xbmc.translatePath(os.path.join(__addonpath__, 'fanart.jpg'))
__addonlanguage__
