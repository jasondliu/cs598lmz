import select
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

from BeautifulSoup import BeautifulSoup

# Addon info
__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonpath__ = __addon__.getAddonInfo('path')
__settings__ = xbmcaddon.Addon(id=__addonid__)
__version__ = __addon__.getAddonInfo('version')
__language__ = __addon__.getLocalizedString

# Global variables
DEBUG = __settings__.getSetting('debug')
if DEBUG == 'true':
    print '*******************************************'
    print 'Addon ID: ' + __addonid__
    print 'Addon Version: ' + __version__
