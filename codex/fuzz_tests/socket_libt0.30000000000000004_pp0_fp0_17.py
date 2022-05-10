import socket
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
__addonpath__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__ = __addon__.getLocalizedString
__resource__ = xbmc.translatePath(os.path.join(__addonpath__, 'resources', 'lib'))

sys.path.append(__resource__)

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

# Global variables
PLUGIN_URL = sys.argv[0]
HANDLE = int(sys.argv[1])

# Plugin handle
_plugin = sys.argv[0]
_handle = int
